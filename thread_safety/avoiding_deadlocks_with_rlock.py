"""
Example demonstrating how to avoid deadlocks using RLock in Python.

This script shows how deadlocks can occur with regular locks and how
threading.RLock (reentrant lock) can be used to avoid them.
"""

import threading
import time

# ===== PART 1: Demonstrating a deadlock with regular locks =====

# Create two regular locks
lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1_function():
    """
    This function acquires lock_a first, then tries to acquire lock_b.
    If thread2_function has already acquired lock_b, this can lead to a deadlock.
    """
    print("Thread 1: Attempting to acquire lock A")
    with lock_a:
        print("Thread 1: Acquired lock A")
        
        # Simulate some work
        time.sleep(0.5)
        
        print("Thread 1: Attempting to acquire lock B")
        with lock_b:
            print("Thread 1: Acquired lock B")
            print("Thread 1: Processing with both locks")

def thread2_function():
    """
    This function acquires lock_b first, then tries to acquire lock_a.
    If thread1_function has already acquired lock_a, this can lead to a deadlock.
    """
    print("Thread 2: Attempting to acquire lock B")
    with lock_b:
        print("Thread 2: Acquired lock B")
        
        # Simulate some work
        time.sleep(0.5)
        
        print("Thread 2: Attempting to acquire lock A")
        with lock_a:
            print("Thread 2: Acquired lock A")
            print("Thread 2: Processing with both locks")

def demonstrate_deadlock():
    """
    Demonstrates how a deadlock can occur with regular locks.
    
    Thread 1 acquires lock A and then tries to acquire lock B.
    Thread 2 acquires lock B and then tries to acquire lock A.
    
    This creates a circular wait condition, leading to a deadlock.
    """
    print("\n=== Demonstrating Deadlock with Regular Locks ===")
    print("This will likely result in a deadlock. Press Ctrl+C to interrupt after a few seconds.")
    
    # Create and start the threads
    t1 = threading.Thread(target=thread1_function)
    t2 = threading.Thread(target=thread2_function)
    
    t1.start()
    t2.start()
    
    # Wait for threads to complete (they likely won't due to deadlock)
    try:
        t1.join(timeout=3)  # Set a timeout to avoid waiting indefinitely
        t2.join(timeout=3)
        
        if t1.is_alive() or t2.is_alive():
            print("\nDeadlock detected! Both threads are still running and waiting for locks.")
            print("In a real application, this would hang indefinitely.")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
    
    print("\nDeadlock Explanation:")
    print("1. Thread 1 acquires lock A and then tries to acquire lock B")
    print("2. Thread 2 acquires lock B and then tries to acquire lock A")
    print("3. Both threads are now waiting for a lock that the other thread holds")
    print("4. Neither thread can proceed, resulting in a deadlock")


# ===== PART 2: Avoiding deadlocks with RLock =====

class NestedLockExample:
    """
    Class demonstrating how RLock allows a thread to acquire the same lock multiple times.
    """
    def __init__(self):
        self.rlock = threading.RLock()
        self.value = 0
    
    def outer_method(self):
        """
        This method acquires the lock and then calls inner_method,
        which also tries to acquire the same lock.
        """
        print(f"Thread {threading.current_thread().name}: Acquiring lock in outer_method")
        try:
            # Use a timeout when acquiring the lock to prevent hanging
            if not self.rlock.acquire(timeout=1):
                print(f"Thread {threading.current_thread().name}: Failed to acquire lock in outer_method (timeout)")
                return
                
            print(f"Thread {threading.current_thread().name}: Lock acquired in outer_method")
            try:
                self.value += 1
                # Call inner_method which will try to acquire the same lock
                self.inner_method()
            finally:
                # Always release the lock, even if an exception occurs
                self.rlock.release()
                print(f"Thread {threading.current_thread().name}: Released lock in outer_method")
        except Exception as e:
            print(f"Thread {threading.current_thread().name}: Error in outer_method: {e}")
    
    def inner_method(self):
        """
        This method also tries to acquire the lock.
        With a regular Lock, this would cause a deadlock if called from outer_method.
        With RLock, it works fine because the same thread can acquire the lock multiple times.
        """
        print(f"Thread {threading.current_thread().name}: Attempting to acquire lock in inner_method")
        try:
            # Use a timeout when acquiring the lock to prevent hanging
            if not self.rlock.acquire(timeout=1):
                print(f"Thread {threading.current_thread().name}: Failed to acquire lock in inner_method (timeout)")
                return
                
            print(f"Thread {threading.current_thread().name}: Lock acquired in inner_method")
            try:
                self.value += 1
                print(f"Thread {threading.current_thread().name}: Value is now {self.value}")
            finally:
                # Always release the lock, even if an exception occurs
                self.rlock.release()
                print(f"Thread {threading.current_thread().name}: Released lock in inner_method")
        except Exception as e:
            print(f"Thread {threading.current_thread().name}: Error in inner_method: {e}")

def demonstrate_rlock_reentrance():
    """
    Demonstrates how RLock allows the same thread to acquire the lock multiple times,
    avoiding deadlocks in nested lock acquisitions.
    """
    print("\n=== Demonstrating RLock Reentrance ===")
    
    example = NestedLockExample()
    
    # Create and start a thread
    t = threading.Thread(name="RLockThread", target=example.outer_method)
    t.start()
    
    # Wait for thread to complete with a timeout to prevent hanging
    try:
        t.join(timeout=3)  # Set a timeout to avoid waiting indefinitely
        
        if t.is_alive():
            print("\nWarning: Thread is still running after timeout.")
            print("This might indicate an issue with the RLock implementation.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    
    print("\nRLock Reentrance Explanation:")
    print("1. The thread acquires the RLock in outer_method")
    print("2. While still holding the lock, it calls inner_method")
    print("3. inner_method tries to acquire the same lock")
    print("4. With a regular Lock, this would deadlock")
    print("5. With RLock, it works because the same thread can acquire the lock multiple times")
    print("6. The lock is only fully released when all acquisitions have been released")


# ===== PART 3: Comparing Lock vs RLock with a practical example =====

class ResourceManager:
    """
    Class demonstrating the difference between Lock and RLock in a practical scenario.
    """
    def __init__(self, use_rlock=False):
        # Use either a regular Lock or an RLock based on the parameter
        self.lock_type = "RLock" if use_rlock else "Lock"
        self.lock = threading.RLock() if use_rlock else threading.Lock()
        self.resource_a = 0
        self.resource_b = 0
    
    def update_resource_a(self):
        """Update resource A and then call update_both_resources."""
        print(f"{self.lock_type} Thread: Acquiring lock for resource A")
        
        # Use explicit lock acquisition with timeout for regular Lock
        acquired = self.lock.acquire(timeout=1 if not isinstance(self.lock, threading.RLock) else None)
        if not acquired:
            print(f"{self.lock_type} Thread: Failed to acquire lock for resource A (timeout)")
            return
            
        try:
            print(f"{self.lock_type} Thread: Lock acquired for resource A")
            self.resource_a += 1
            time.sleep(0.1)  # Simulate some work
            
            # Now try to update both resources
            print(f"{self.lock_type} Thread: Calling update_both_resources from update_resource_a")
            self.update_both_resources()
        finally:
            # Always release the lock, even if an exception occurs
            self.lock.release()
            print(f"{self.lock_type} Thread: Released lock for resource A")
    
    def update_resource_b(self):
        """Update resource B only."""
        print(f"{self.lock_type} Thread: Acquiring lock for resource B")
        
        # Use explicit lock acquisition with timeout for regular Lock
        acquired = self.lock.acquire(timeout=1 if not isinstance(self.lock, threading.RLock) else None)
        if not acquired:
            print(f"{self.lock_type} Thread: Failed to acquire lock for resource B (timeout)")
            return
            
        try:
            print(f"{self.lock_type} Thread: Lock acquired for resource B")
            self.resource_b += 1
            time.sleep(0.1)  # Simulate some work
        finally:
            # Always release the lock, even if an exception occurs
            self.lock.release()
            print(f"{self.lock_type} Thread: Released lock for resource B")
    
    def update_both_resources(self):
        """Update both resources A and B."""
        print(f"{self.lock_type} Thread: Acquiring lock for both resources")
        
        # For regular Lock, this will cause a deadlock if called from update_resource_a
        # Use a short timeout to detect and handle the deadlock
        timeout = 1 if not isinstance(self.lock, threading.RLock) else None
        acquired = self.lock.acquire(timeout=timeout)
        
        if not acquired:
            print(f"{self.lock_type} Thread: Failed to acquire lock for both resources (timeout)")
            print(f"{self.lock_type} Thread: This demonstrates the deadlock with regular Lock")
            print(f"{self.lock_type} Thread: With a regular Lock, the same thread cannot acquire the lock it already holds")
            return
            
        try:
            print(f"{self.lock_type} Thread: Lock acquired for both resources")
            self.resource_a += 1
            self.resource_b += 1
            time.sleep(0.1)  # Simulate some work
            print(f"{self.lock_type} Thread: Resources updated - A: {self.resource_a}, B: {self.resource_b}")
        finally:
            # Always release the lock, even if an exception occurs
            self.lock.release()
            print(f"{self.lock_type} Thread: Released lock for both resources")

def demonstrate_lock_vs_rlock():
    """
    Demonstrates the difference between Lock and RLock in a practical scenario.
    """
    print("\n=== Comparing Lock vs RLock ===")
    
    # First demonstrate with regular Lock (will show deadlock with timeout)
    print("\n--- Using Regular Lock ---")
    manager_with_lock = ResourceManager(use_rlock=False)
    
    try:
        print("This will demonstrate a deadlock situation with regular Lock.")
        print("The script will detect the deadlock and continue after a timeout.")
        manager_with_lock.update_resource_a()
    except KeyboardInterrupt:
        print("\nOperation with Lock interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred during Lock demonstration: {e}")
    finally:
        print("\nLock demonstration completed. Notice how it couldn't acquire the lock twice.")
    
    # Then demonstrate with RLock (will work correctly)
    print("\n--- Using RLock ---")
    try:
        manager_with_rlock = ResourceManager(use_rlock=True)
        manager_with_rlock.update_resource_a()
        print("\nRLock demonstration completed successfully.")
    except Exception as e:
        print(f"\nAn error occurred during RLock demonstration: {e}")
    finally:
        print("Notice how RLock allows the same thread to acquire the lock multiple times.")
    
    print("\nLock vs RLock Explanation:")
    print("1. With a regular Lock:")
    print("   - When update_resource_a acquires the lock")
    print("   - And then calls update_both_resources which tries to acquire the same lock")
    print("   - It results in a deadlock (the thread is waiting for a lock it already holds)")
    print("2. With an RLock:")
    print("   - The same thread can acquire the lock multiple times")
    print("   - So update_both_resources can acquire the lock even though update_resource_a already holds it")
    print("   - This prevents the deadlock and allows the operations to complete")


def main():
    """Main function to run all demonstrations."""
    print("Starting deadlock and RLock demonstrations...\n")
    
    # Part 1: Demonstrate deadlock with regular locks
    demonstrate_deadlock()
    
    # Part 2: Demonstrate RLock reentrance
    demonstrate_rlock_reentrance()
    
    # Part 3: Compare Lock vs RLock
    demonstrate_lock_vs_rlock()
    
    print("\nSummary:")
    print("1. Deadlocks occur when threads are waiting for resources held by each other")
    print("2. Regular Lock objects can cause deadlocks in nested lock acquisitions")
    print("3. RLock (reentrant lock) allows the same thread to acquire the lock multiple times")
    print("4. Use RLock when a thread might need to acquire the same lock multiple times")
    print("   (e.g., in recursive functions or when methods call other methods that use the same lock)")
    print("5. RLock keeps track of which thread owns it and how many times it's been acquired")
    print("6. The lock is only fully released when all acquisitions have been released")

if __name__ == "__main__":
    main()