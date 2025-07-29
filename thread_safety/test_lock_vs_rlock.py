"""
Simple test script to verify that the avoiding_deadlocks_with_rlock.py script
runs without getting stuck in Part 3 (Lock vs RLock comparison).
"""

import sys
import time
import threading
from contextlib import redirect_stdout
import io

# Import the function we want to test
sys.path.append('.')
from avoiding_deadlocks_with_rlock import demonstrate_lock_vs_rlock

def test_lock_vs_rlock():
    """
    Test the demonstrate_lock_vs_rlock function to ensure it doesn't get stuck.
    """
    print("Testing Lock vs RLock demonstration...")
    
    # Capture stdout to prevent cluttering the console
    f = io.StringIO()
    with redirect_stdout(f):
        # Set a timeout for the entire test
        start_time = time.time()
        
        # Run the function in a separate thread so we can monitor it
        thread = threading.Thread(target=demonstrate_lock_vs_rlock)
        thread.start()
        
        # Wait for the thread to complete with a timeout
        thread.join(timeout=10)  # Give it a bit more time since it's demonstrating both Lock and RLock
        
        end_time = time.time()
        
        # Check if the thread is still running
        if thread.is_alive():
            print("ERROR: The demonstrate_lock_vs_rlock function is still running after 10 seconds.")
            print("This indicates that it might be stuck in a deadlock or infinite loop.")
            return False
        
    # Get the captured output
    output = f.getvalue()
    
    # Check if the function completed successfully
    if "Lock vs RLock Explanation" in output and "RLock demonstration completed successfully" in output:
        print("SUCCESS: The demonstrate_lock_vs_rlock function completed successfully.")
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        print("\nOutput highlights:")
        
        # Extract and print key parts of the output
        if "Lock Thread: Failed to acquire lock for both resources (timeout)" in output:
            print("- Successfully detected deadlock with regular Lock")
        if "RLock Thread: Lock acquired for both resources" in output:
            print("- Successfully acquired lock multiple times with RLock")
        
        return True
    else:
        print("ERROR: The demonstrate_lock_vs_rlock function did not complete successfully.")
        print("Output:", output)
        return False

if __name__ == "__main__":
    result = test_lock_vs_rlock()
    sys.exit(0 if result else 1)