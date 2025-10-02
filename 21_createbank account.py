class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}, New Balance = {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdraw {amount}, New Balance = {self.balance}"

    def check_balance(self):
        return f"Balance = {self.balance}"


acc = BankAccount(1000)
print(acc.deposit(500))
print(acc.withdraw(200))
print(acc.check_balance())
