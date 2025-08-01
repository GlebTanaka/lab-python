import time
import threading
from concurrent.futures import ThreadPoolExecutor
from itertools import batched

# Fixed delay for demonstration purposes
DELAY = 0.05

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        # Create a threading.Lock object for this account
        # This lock will ensure that only one thread can access the account at a time
        self.account_lock = threading.Lock()

    def withdraw(self, amount):
        """
        Thread-safe method to withdraw money from the account.
        Uses a lock to prevent race conditions.

        How it works:
        1. Acquires the lock before accessing the balance
        2. Only one thread can hold the lock at a time
        3. Other threads must wait until the lock is released
        4. The 'with' statement ensures the lock is always released
        """
        # The 'with' statement automatically acquires and releases the lock
        # This is safer than manual lock.acquire() and lock.release()
        with self.account_lock:
            # Critical section - only one thread can execute this at a time
            if self.balance >= amount:
                new_balance = self.balance - amount
                time.sleep(DELAY)  # Simulate a delay
                self.balance = new_balance
            else:
                raise ValueError("Insufficient balance")
        # Lock is automatically released when leaving the 'with' block

    def deposit(self, amount):
        """
        Thread-safe method to deposit money into the account.
        Uses the same lock as withdraw() to prevent race conditions.

        Even though deposit() and withdraw() are different methods,
        they use the same lock (self.account_lock) to ensure that
        all operations on the account are synchronized.
        """
        with self.account_lock:
            # Critical section - protected by the lock
            new_balance = self.balance + amount
            time.sleep(DELAY)  # Simulate a delay
            self.balance = new_balance
        # Lock is automatically released here

def charge_fees():
    """
    Charges fees to all accounts.
    Thread-safe because each account has its own lock.
    Different threads can process different accounts concurrently,
    but operations on the same account are serialized.
    """
    for account in accounts:
        account.withdraw(14.95)

def reimburse_fees():
    """
    Reimburses fees to all accounts.
    Also thread-safe due to per-account locks.
    """
    for account in accounts:
        account.deposit(14.95)

# ---------------------------------------------------------------------

print("Creating accounts")
# Create 50 accounts, each with its own lock
accounts = [BankAccount(1000) for _ in range(0, 50)]

print("Charging fees")
# Create a thread pool and submit both operations to run concurrently
# Even though operations run concurrently, the locks prevent race conditions
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(charge_fees)      # Thread 1: Withdraws 14.95
    executor.submit(reimburse_fees)   # Thread 2: Deposits 14.95

print("Checking balances")
# Print final balances - they should all be exactly 1000
# Because the locks ensure that both withdrawal and deposit are processed correctly
for account_set in batched(accounts, 5):
    for account in account_set:
        print(f"{account.balance:7.2f}   ", end='')
    print()

"""
Key Points About This Implementation:

1. Each account has its own lock
   - This allows operations on different accounts to proceed in parallel
   - Only operations on the same account are serialized

2. The lock protects the entire operation
   - Both reading and writing the balance are inside the critical section
   - The artificial delay is also inside the critical section
   - This ensures that no other thread can interfere during the entire operation

3. Using 'with' statement for lock management
   - Automatically releases the lock even if an exception occurs
   - Prevents deadlocks from forgotten lock releases
   - More readable than explicit acquire/release calls

4. Results
   - All accounts should end with exactly 1000
   - No race conditions possible because locks prevent concurrent access
   - May be slightly slower than non-locked version due to lock overhead

5. Compare with non-locked version
   - This version: Always correct, slightly slower
   - Non-locked version: Fast but prone to race conditions and data corruption
"""