import sys
import time
from concurrent.futures import ThreadPoolExecutor
from itertools import batched

# Command line argument for delay - this makes race conditions more likely to occur
DELAY = float(sys.argv[1])

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account. This method is susceptible to race conditions
        because it performs a read-modify-write operation with a delay in between.

        Race condition scenario:
        1. Thread A reads balance=1000
        2. Thread B reads balance=1000
        3. Thread A calculates new_balance=985.05 (1000 - 14.95)
        4. Thread B calculates new_balance=985.05 (1000 - 14.95)
        5. Thread A writes balance=985.05
        6. Thread B writes balance=985.05

        Result: Only one withdrawal is recorded instead of two!
        """
        if self.balance >= amount:
            # RACE CONDITION POINT 1: Reading the balance
            # Multiple threads can read the same initial balance
            new_balance = self.balance - amount

            # Artificial delay to make race conditions more likely
            time.sleep(DELAY)

            # RACE CONDITION POINT 2: Writing the balance
            # Multiple threads might write their calculated balance,
            # potentially overwriting each other's changes
            self.balance = new_balance
        else:
            raise ValueError("Insufficient balance")

    def deposit(self, amount):
        """
        Deposits money into the account. This method has the same race condition
        vulnerability as withdraw().

        Race condition scenario:
        1. Thread A reads balance=985.05
        2. Thread B reads balance=985.05
        3. Thread A calculates new_balance=1000 (985.05 + 14.95)
        4. Thread B calculates new_balance=1000 (985.05 + 14.95)
        5. Thread A writes balance=1000
        6. Thread B writes balance=1000

        Result: Only one deposit is recorded instead of two!
        """
        # RACE CONDITION POINT 1: Reading the balance
        new_balance = self.balance + amount

        # Artificial delay to make race conditions more likely
        time.sleep(DELAY)

        # RACE CONDITION POINT 2: Writing the balance
        self.balance = new_balance

def charge_fees():
    """Charges fees to all accounts. Called by one thread."""
    for account in accounts:
        account.withdraw(14.95)

def reimburse_fees():
    """Reimburses fees to all accounts. Called by another thread."""
    for account in accounts:
        account.deposit(14.95)

# ---------------------------------------------------------------------

print("Creating accounts")
# Create 50 accounts with initial balance of 1000 each
accounts = [BankAccount(1000) for _ in range(0, 50)]

print("Charging fees")
# Create a thread pool and submit both operations to run concurrently
# This is where race conditions can occur since both threads access
# the same accounts simultaneously
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(charge_fees)      # Thread 1: Withdraws 14.95
    executor.submit(reimburse_fees)   # Thread 2: Deposits 14.95

print("Checking balances")
# Print final balances - due to race conditions, they might not all be 1000
# If you see values different from 1000, that's evidence of a race condition
for account_set in batched(accounts, 5):
    for account in account_set:
        print(f"{account.balance:7.2f}   ", end='')
    print()

"""
How to reproduce race conditions:
1. Run with a small delay (e.g., 0.001 seconds):
   python bank.py 0.001
   - May see some race conditions, but not always

2. Run with a larger delay (e.g., 0.1 seconds):
   python bank.py 0.1
   - More likely to see race conditions due to longer window of vulnerability

Expected behavior without race conditions:
- Each account should end up with 1000 (initial balance)
- Because: 1000 - 14.95 + 14.95 = 1000

Actual behavior with race conditions:
- Accounts may show different balances
- Common values: 985.05 (only withdrawal recorded) or 1014.95 (only deposit recorded)
"""