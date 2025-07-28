"""
Example demonstrating threads and race conditions in Python.

This script shows how multiple threads can lead to race conditions
when they access and modify shared data without proper synchronization.
"""

import threading
import time
import random

# Shared resource - a counter that will be accessed by multiple threads
counter = 0
iterations = 100000

def increment_counter():
    """
    Function that increments the shared counter.
    This demonstrates a race condition when called from multiple threads.
    """
    global counter
    
    print(f"Thread {threading.current_thread().name} starting...")
    
    for _ in range(iterations):
        # Read the current value
        current_value = counter
        # Simulate some processing time (makes race condition more likely)
        if random.random() < 0.000001:
            time.sleep(0.000001)
        # Increment and write back
        counter = current_value + 1
    
    print(f"Thread {threading.current_thread().name} finished.")

def main():
    # Reset counter
    global counter
    counter = 0
    
    print("Starting race condition demonstration...")
    print(f"Expected final counter value: {iterations * 2}")
    
    # Create two threads that will increment the counter
    thread1 = threading.Thread(name="Thread-1", target=increment_counter)
    thread2 = threading.Thread(name="Thread-2", target=increment_counter)
    
    # Start the threads
    start_time = time.time()
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    end_time = time.time()
    
    # Print the final counter value
    print(f"Final counter value: {counter}")
    print(f"Missing increments: {iterations * 2 - counter}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    
    # Explain the race condition
    if counter < iterations * 2:
        print("\nRace Condition Explanation:")
        print("1. Thread 1 reads the counter value (e.g., 500)")
        print("2. Thread 2 reads the same counter value (500)")
        print("3. Thread 1 increments and writes back (501)")
        print("4. Thread 2 increments its read value and writes back (501)")
        print("5. Instead of getting 502, we still have 501 - one increment was lost!")
        print("\nThis happens because the increment operation is not atomic.")
        print("It consists of three steps: read, modify, and write.")
        print("When these steps interleave between threads, data corruption occurs.")

if __name__ == "__main__":
    main()