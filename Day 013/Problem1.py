# Question: Create a Class for a Bank Account Task: Write a Python program to create a BankAccount class with methods to deposit and withdraw money, as well as check the balance.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

# Example usage:
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.check_balance()
