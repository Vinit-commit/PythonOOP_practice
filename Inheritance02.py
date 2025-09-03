# encapsulation in python

# _ -> protected
# __ -> private


class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner  # Public attribute
        self._account_number = "12345" # Protected attribute
        self.__balance = starting_balance # Private attribute

    def deposit(self, amount):
        """Adds money to the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    def display_balance(self):
        """Provides controlled access to the balance."""
        print(f"Account for {self.owner} has a balance of ${self.__balance}")

# --- Let's use the class ---
my_account = BankAccount("Rohan Kumar", 5000)

# 1. Using the public methods (The correct way ✅)
my_account.display_balance()
my_account.deposit(1500)
my_account.withdraw(500)
my_account.withdraw(10000) # This will fail safely

print("-" * 20)

# 2. Accessing public and protected attributes
print(f"Account Owner: {my_account.owner}") # Public: OK to access
print(f"Account Number: {my_account._account_number}") # Protected: Works, but bad practice

print("-" * 20)

# 3. Trying to access the private attribute (This will FAIL)
try:
    print(my_account.__balance)
except AttributeError as e:
    print(f"Error: {e}")

# Python has renamed it (name mangling). You can still access it if you know the name.
# This shows it's not truly private, just hidden.
print(f"The mangled name is _BankAccount__balance: ${my_account._BankAccount__balance}")
print(my_account._account_number)