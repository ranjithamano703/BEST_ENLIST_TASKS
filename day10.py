class Bank:
    def __init__(self):
        self.balance=0
        print("the account is created")
    def deposit(self):
        amount=float(input("Enter the amount to be deposit:"))
        self.balance = self.balance+amount
        print("Deposit is successful and the balance in the account is %f" % self.balance)
    def withdraw(self):
        amount=float(input("Enter the amount to withdraw: "))
        if(self.balance >= amount):
            self.balance = self.balance-amount
            print("the withdraw is successfull and balance is %f" % self.balance)
        else:
            print("insuficient balance")
    def enquiry(self):
        print("Balance in the amount is %f" %self.balance) 
acc= Bank()
acc.deposit()
acc.withdraw()
