"""
Simple test script to verify that the avoiding_deadlocks_with_rlock.py script
runs without getting stuck in Part 2.
"""

import sys
import time
import threading
from contextlib import redirect_stdout
import io

# Import the function we want to test
sys.path.append('.')
from avoiding_deadlocks_with_rlock import demonstrate_rlock_reentrance

def test_rlock_reentrance():
    """
    Test the demonstrate_rlock_reentrance function to ensure it doesn't get stuck.
    """
    print("Testing RLock reentrance demonstration...")
    
    # Capture stdout to prevent cluttering the console
    f = io.StringIO()
    with redirect_stdout(f):
        # Set a timeout for the entire test
        start_time = time.time()
        
        # Run the function in a separate thread so we can monitor it
        thread = threading.Thread(target=demonstrate_rlock_reentrance)
        thread.start()
        
        # Wait for the thread to complete with a timeout
        thread.join(timeout=5)
        
        end_time = time.time()
        
        # Check if the thread is still running
        if thread.is_alive():
            print("ERROR: The demonstrate_rlock_reentrance function is still running after 5 seconds.")
            print("This indicates that it might be stuck in a deadlock or infinite loop.")
            return False
        
    # Get the captured output
    output = f.getvalue()
    
    # Check if the function completed successfully
    if "RLock Reentrance Explanation" in output:
        print("SUCCESS: The demonstrate_rlock_reentrance function completed successfully.")
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        return True
    else:
        print("ERROR: The demonstrate_rlock_reentrance function did not complete successfully.")
        print("Output:", output)
        return False

if __name__ == "__main__":
    result = test_rlock_reentrance()
    sys.exit(0 if result else 1)