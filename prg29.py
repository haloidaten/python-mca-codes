
class bankacc:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account number:", self.acc_no)
        print("Name:", self.name)
        print("Account type:", self.acc_type)
        print("Balance:", self.balance)


b1 = bankacc(101, "Arun", "Savings", 5000)

b1.display()
b1.deposit(2000)
b1.withdraw(1000)
