class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        self.balance += amount
        return f"Deposited ${amount}. New balance is ${self.balance}."

    def withdraw(self, amount): 
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Available balance is ${self.balance}.")
        self.balance -= amount
        return f"Withdrew ${amount}. New balance is ${self.balance}."

    def get_balance(self):
        return f"Your current balance is ${self.balance}."

