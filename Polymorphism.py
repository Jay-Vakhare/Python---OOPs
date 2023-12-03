class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        pass  # To be overridden in the derived classes


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def display_balance(self):
        super().display_balance()
        print(f"Interest Rate: {self.interest_rate}%")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Invalid withdrawal amount.")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def display_balance(self):
        super().display_balance()
        print(f"Overdraft Limit: ${self.overdraft_limit}")

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Invalid withdrawal amount.")

# Example usage:
savings_account = SavingsAccount(account_number=1001, balance=5000, interest_rate=2.5)
checking_account = CheckingAccount(account_number=2001, balance=7000, overdraft_limit=1000)

print("Savings Account Details:")
savings_account.display_balance()
savings_account.withdraw(1000)

print("\nChecking Account Details:")
checking_account.display_balance()
checking_account.withdraw(8000)
