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

bankaccount1 = BankAccount(0.05, 100)
bankaccount2 = BankAccount(0.03, 200)

bankaccount1.deposit(10).deposit(20).deposit(30).withdraw(10).yield_interest().display_account_info()
bankaccount2.deposit(10).deposit(20).withdraw(15).withdraw(15).withdraw(15).withdraw(15).yield_interest().display_account_info()

BankAccount.print_all_accounts()