'''
1)c)Guido Van Rossum
2)c)[3,4]
3)a)import module_name
4)b)#
5)c)lambda
6)b
7)a
8)c
9)a
10)b
'''
#11)
'''
num=[1,2,3,4,5,6]
squares=[i**2 for i in num]
print(squares)
'''
#12)
'''
list1=[2,4,6,8,3,5]
def second_large():
    list1.sort()
    print(list1[-2])
second_large()
'''
#13)
'''
list1=[3,6,3,7,9,9,8,5,2,7,2,3]
def new_list():
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
new_list()
'''
#14)
'''
x=(1,2,3,4,5,6,7)
def reverse_order():
    y=list(x)
    y.reverse()
    x=tuple(y)
    print(x)
reverse_order()
'''
#16)
'''
set1={1,2,3}
set2={4,5,6}
def disjoint():
    print(set1.isdisjoint(set2))
disjoint()
'''
#17)
'''
dict1={
    1:"aby",
    2:"boby",
    3:"cherry",
    4:"john",
    5:"mary"
    }
dict2={}
def swap():
    for i,j in dict1.items():
        if j in dict2:
            dict2[j].append(i)
        else:
            dict2[j]=(i)
    print(dict2)
swap()
'''
#19)
'''
def factorial():
    num=int(input("enter a number:"))
    fact=1
    i=1
    while i<=num:
        fact*=i
        i+=1
    print(fact)
factorial()
'''
#20)
'''
num=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x: x%2==0,num)
print(list(even))
'''
#21)
'''
number=[4]
square=map(lambda x: x**2,number)
print(list(square))
'''
#23)
'''
x="Python Program to Count the Number of Vowels in a String"
y=x.split()
vowel="aeiou"
def vowels():
    for i in range(0,len(i)):
      if 
'''        
#24)
'''
x="PYTHON PROGRAM TO COUNT THE Number of Vowels in a String"        
def lower_case():
    y=x.casefold()
    print(y)
lower_case()
'''
#28)
'''
string=input("enter a word:")
def palindrom():
    if string==string[::-1]:
        print("it is palindrome")
    else:
        print("not a palindrom")
palindrom()
'''
#26)
'''
class Bank():
    def __init__(self,account_no,customer_name,balance):
        self.account_no=account_no
        self.customer_name=customer_name
        self.balance=balance
    def new_deposit(self):
        deposit=int(input("enter an amount:"))
        current_deposit=self.balance+deposit
        print(current_deposit)
    def to_withdraw(self):
        withdraw=int(input("enter the withdraw amount:"))
        if withdraw<self.balance:
            current_amount=self.balance-withdraw
            print(current_amount)
        else:
            print("insufficient balance")
    def current_balance(self):
        print(self.balance)
obj1=Bank(202,"ajay",10000)
obj1.new_deposit()
obj1.to_withdraw()
obj1.current_balance()
'''           











































