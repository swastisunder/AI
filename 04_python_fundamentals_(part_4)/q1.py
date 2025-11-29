'''
Create a BankAccount class with attributes account_number owner_name, and balance
Add methods deposit withdraw check balance
'''

class BankAccount:
    def __init__(self,account_number,owner_name):
        self.account_number=account_number
        self.owner_name=owner_name
        self.__balance=0
    
    def deposit(self,amount):
        self.__balance+=amount
        print(f"{amount} added. Now your balance is {self.__balance}")
    
    def withdraw(self,amount):
        self.__balance-=amount
        print(f"{amount} deducted. Now your balance is {self.__balance}")
    
    def check_balance(self):
        print(f"Your Balance is : {self.__balance}")
        
a = BankAccount(1,'ssb')
a.deposit(5000)
a.withdraw(1000)
a.check_balance()