class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

#Example

bank = Bank("Bank", 1000)

bank.deposit(1000)
bank.withdraw(700)
print(bank.balance) # Output: 1300