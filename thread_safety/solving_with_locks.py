"""
Example demonstrating how to solve race conditions using locks in Python.

This script shows how to use threading.Lock to protect shared resources
and prevent race conditions when multiple threads access and modify shared data.
"""

import threading
import time
import random

# Shared resources
counter_without_lock = 0
counter_with_lock = 0
iterations = 100000

# Create a lock object
counter_lock = threading.Lock()

def increment_without_lock():
    """
    Function that increments the shared counter without using a lock.
    This will demonstrate a race condition.
    """
    global counter_without_lock
    
    for _ in range(iterations):
        # Read the current value
        current_value = counter_without_lock
        # Simulate some processing time (makes race condition more likely)
        if random.random() < 0.000001:
            time.sleep(0.000001)
        # Increment and write back
        counter_without_lock = current_value + 1

def increment_with_lock():
    """
    Function that increments the shared counter using a lock.
    This will prevent race conditions.
    """
    global counter_with_lock
    
    for _ in range(iterations):
        # Acquire the lock before accessing the shared resource
        counter_lock.acquire()
        try:
            # Critical section - protected by the lock
            current_value = counter_with_lock
            # Simulate some processing time (same as without lock)
            if random.random() < 0.000001:
                time.sleep(0.000001)
            counter_with_lock = current_value + 1
        finally:
            # Always release the lock, even if an exception occurs
            counter_lock.release()

def increment_with_lock_context_manager():
    """
    Alternative function that uses a context manager (with statement)
    to acquire and release the lock. This is the recommended approach.
    """
    global counter_with_lock
    
    for _ in range(iterations):
        # Use context manager to handle lock acquisition and release
        with counter_lock:
            # Critical section - protected by the lock
            current_value = counter_with_lock
            # Simulate some processing time
            if random.random() < 0.000001:
                time.sleep(0.000001)
            counter_with_lock = current_value + 1

def run_without_lock():
    """Run the demonstration without using locks."""
    global counter_without_lock
    counter_without_lock = 0
    
    print("\n--- Without Lock ---")
    print(f"Expected final counter value: {iterations * 2}")
    
    # Create two threads
    thread1 = threading.Thread(target=increment_without_lock)
    thread2 = threading.Thread(target=increment_without_lock)
    
    # Start the threads
    start_time = time.time()
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    end_time = time.time()
    
    # Print the results
    print(f"Final counter value: {counter_without_lock}")
    print(f"Missing increments: {iterations * 2 - counter_without_lock}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")

def run_with_lock():
    """Run the demonstration using locks."""
    global counter_with_lock
    counter_with_lock = 0
    
    print("\n--- With Lock ---")
    print(f"Expected final counter value: {iterations * 2}")
    
    # Create two threads
    thread1 = threading.Thread(target=increment_with_lock)
    thread2 = threading.Thread(target=increment_with_lock)
    
    # Start the threads
    start_time = time.time()
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    end_time = time.time()
    
    # Print the results
    print(f"Final counter value: {counter_with_lock}")
    print(f"Missing increments: {iterations * 2 - counter_with_lock}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")

def run_with_lock_context_manager():
    """Run the demonstration using locks with context manager."""
    global counter_with_lock
    counter_with_lock = 0
    
    print("\n--- With Lock (Context Manager) ---")
    print(f"Expected final counter value: {iterations * 2}")
    
    # Create two threads
    thread1 = threading.Thread(target=increment_with_lock_context_manager)
    thread2 = threading.Thread(target=increment_with_lock_context_manager)
    
    # Start the threads
    start_time = time.time()
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    end_time = time.time()
    
    # Print the results
    print(f"Final counter value: {counter_with_lock}")
    print(f"Missing increments: {iterations * 2 - counter_with_lock}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")

def main():
    print("Starting lock demonstration...")
    
    # Run the demonstration without locks
    run_without_lock()
    
    # Run the demonstration with locks
    run_with_lock()
    
    # Run the demonstration with locks using context manager
    run_with_lock_context_manager()
    
    print("\nLock Explanation:")
    print("1. Without a lock: Both threads can access the counter simultaneously,")
    print("   leading to race conditions and lost updates.")
    print("2. With a lock: Only one thread can access the counter at a time,")
    print("   ensuring that all updates are properly recorded.")
    print("3. The context manager approach (with statement) is recommended as it")
    print("   automatically handles lock release, even if exceptions occur.")
    print("\nNote: Using locks may increase execution time due to the overhead")
    print("of lock acquisition and release, but it ensures data integrity.")

if __name__ == "__main__":
    main()