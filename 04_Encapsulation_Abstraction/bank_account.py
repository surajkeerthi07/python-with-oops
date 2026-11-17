# CRT Program 20: Basic bank account class

class BankAccount:
    def __init__(self, holder_name, account_number, balance=0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print("Deposited:", amount)
        print("Updated balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Updated balance:", self.balance)

    def display_balance(self):
        print("Account holder:", self.holder_name)
        print("Account number:", self.account_number)
        print("Balance:", self.balance)


account = BankAccount("Suhasi", "24/256749", 20000)
account.deposit(200)
account.withdraw(300)
account.display_balance()
