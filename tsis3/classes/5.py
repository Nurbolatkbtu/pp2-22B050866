class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,money):
        self.balance += money
    def withdraw(self,money):
        self.balance -= money
        if self.balance < 0:
            print("You haven't enough money")
        else:
            print(self.balance)
a = Account("Abylaikhan",5000)
a.deposit(3000)
a.withdraw(6000)
