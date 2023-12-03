from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: Rs {self.balance}")

class SavingsAccount(Bank):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs {amount} into Savings Account")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew Rs {amount} from Savings Account")
        else:
            print("Insufficient funds")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added Rs {interest} interest to Savings Account")

class CheckingAccount(Bank):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs {amount} into Checking Account")

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew Rs {amount} from Checking Account")
        else:
            print("Insufficient funds (including overdraft)")

# Example Usage
savings_account = SavingsAccount(account_number="S12345", balance=1000)
savings_account.deposit(500)
savings_account.display_balance()
savings_account.withdraw(200)
savings_account.add_interest()
savings_account.display_balance()

checking_account = CheckingAccount(account_number="C67890", balance=500, overdraft_limit=200)
checking_account.display_balance()
checking_account.withdraw(700)
checking_account.display_balance()
