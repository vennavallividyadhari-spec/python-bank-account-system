class Account:
    bank="HDFC Bank"#class attribute
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
        print("Welcome to HDFC Bank!")
    def debit(self,debit_amount):
        if(self.balance>=debit_amount):
            self.balance=self.balance-debit_amount
            print("Amount Debited:",format(debit_amount,",.2f"))
        else:
            print("Insuffient Balance")
    def credit(self,credit_amount):
        limit=100000.00
        if(credit_amount>limit):
            print("Credit Limit Exceeded!")
        else:
            self.balance=self.balance+credit_amount
            print("Amount Credited:",format(credit_amount,",.2f"))
       
    def check_balance(self):
        print("Your current Balance is:",format(self.balance,",.2f"))
c1=Account(500000,12345)
c1.debit(2000)
c1.credit(1000)
c1.check_balance()
