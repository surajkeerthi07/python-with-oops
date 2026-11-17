# CRT Program 13: Hierarchical inheritance

class Account:
    def account_number(self):
        print("Account number: 123456")


class SavingsAccount(Account):
    def credit(self):
        print("Money credited to savings account")


class CurrentAccount(Account):
    def withdraw(self):
        print("Money withdrawn from current account")


savings = SavingsAccount()
savings.account_number()
savings.credit()

current = CurrentAccount()
current.account_number()
current.withdraw()
