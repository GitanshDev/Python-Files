# Basics of Bank Account Managament

class Account:

    def __init__(self, balance, acc):
        self.balance = balance
        self.Account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("₹", amount, "was debited")
        print("Total Balance:-",self.balance)

    def credit(self, amount):
        self.balance += amount
        print("₹", amount, "was credited")
        print("Total Balance:-",self.balance)


    def fin_bal(self):
        return self.balance

Acc1 = Account(float(input("Enter Your Balance:- ")), "ACCXXX")
print("Your Balance is:",Acc1.balance)
Acc1.credit(int(input("Enter Your Credit:- ")))
Acc1.debit(int(input("Enter Your Debit:- ")))