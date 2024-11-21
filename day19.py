#4 pillers of Ooops:
'''
class Animal():
    def __init__(self,name):
        self.animalname=name
class Cat(Animal):
    def speek(self):
        print("mwow")
class Cow(Animal):
    #super function:
    def __init__(self,name,age):
        super(). __init__(name)
        self.animal_age=age
    def speek(self):
        print("moo")
obj1=Animal("buby")
obj2=Cat("pink")
obj3=Cow("daisy",20)
obj2.speek()
obj3.speek()
'''
class Bank_account():
    def __init___(self,account_no,customer_name,balance,creation_date):
        self.account_no=account_no
        self.customer_name=customer_name
        self.balance=balance
        self.creation_date="12/12/2024"
    def new_deposit(self):
        deposit=int(input("enter the amount"))
        current_deposit=self.balance+deposit
        print(f"balance={current_deposit}")
    def to_withdraw(self):
        withdraw=int(input("enter the amount"))
        if withdraw<self.balance:
            current_amount=self.balance-withdraw
            print(f"balance:{current_amount}")
        else:
            print("insufficient balance")
    def current_balance(self):
        print(f"balance:{self.balance}")
    def customer_details(self):
        print(f"customer name: {self.customer_name}")
        print(f"account no: {self.account_no}")
        print(f"creation date: {self.creation_date}")
        print(f"balance amount: {self.balance}")
obj1=Bank_account(220222, "rafeedha",1000)
obj1=new_deposit()
#obj1=to_withdraw()
#obj1=current_balance()
obj1=customer_details()


        
        
        
    

