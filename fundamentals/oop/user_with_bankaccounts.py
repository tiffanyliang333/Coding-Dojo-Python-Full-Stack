class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance < amount:
            print(f'Insufficient funds: Charging a $5 fee.')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

# bankaccount1 = BankAccount(0.05, 100)
# bankaccount2 = BankAccount(0.03, 200)

# bankaccount1.deposit(10).deposit(20).deposit(30).withdraw(10).yield_interest().display_account_info()
# bankaccount2.deposit(10).deposit(20).withdraw(15).withdraw(15).withdraw(15).withdraw(15).yield_interest().display_account_info()

# BankAccount.print_all_accounts()

class User:
    def __init__(self, name, email, account_type):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.account_type = account_type

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account.balance < amount:
            print(f'Insufficient funds: Charging a $5 fee.')
            self.account.balance -= 5
        else:
            self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f'User: {self.name}, {self.account_type} Balance: {self.account.balance}')
        return self

# tiffanyAccount = User('Tiffany', 'xyz@gmail.com')
# saraAccount = User ('Sara', 'abc@gmail.com')

# tiffanyAccount.make_deposit(10).display_user_balance()
# saraAccount.make_deposit(30).display_user_balance()

# tiffanyAccount.make_withdrawal(100).display_user_balance()
# saraAccount.make_withdrawal(10).display_user_balance()

tiffanyCheckingAccount = User('Tiffany', 'xyz@gmail.com', 'Checking')
tiffanySavingsAccount = User('Tiffany', 'xyz@gmail.com', 'Savings')
saraCheckingAccount = User('Sara', 'abc@gmail.com', 'Checking')
saraSavingsAccount = User('Sara', 'abc@gmail.com', 'Savings')

tiffanyCheckingAccount.make_deposit(10).display_user_balance()
tiffanySavingsAccount.make_deposit(50).display_user_balance()