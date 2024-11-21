#print("my"+"name"+"is rafeedham pc")
#print("bye"*6)

#question:1
'''
salary= int(input("enter your salary:"))
year=int (input("enter your year of service"))
if year>5:
    print(f"{salary+salary*0.05}")
else:
    print("not eligible")
'''

#question 2:
"""
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
if length==breadth:
    print("it is a square")
else:
    print(" not a square, it is rectangle")
"""
#question 3:
'''
x=int(input("enter an integer number"))
y=int(input("enter another integer number"))
if x<y:
    print(f"{y}is greatest")
else:
    print(f"{x} is greatest")
'''
#Write a program that calculates the factorial of a number using a
#while loop.
"""

x=int(input("enter a number"))
p=1
i=1
while i<=x:
    p*=i
    i+=1
print(p)
"""
#Write a Python program that uses a while loop to print numbers from
#1 to 10
'''
i=1
while i<=10: 
    print (i)
    i+=1
print("end")
'''
#How would you modify the previous program to print only even
#numbers using a continue statement?
'''

i = 1
while i<=10:
    if i%2!=0:
        i+=1
        continue
    print(i)
    i+=1
print("end")
'''
#Create a program that asks the user to enter a password using a while loop. The loop should continue until the correct password is entered and terminate if the user enters 'quit'.
'''

password="text@123"
while True:
    user_password=input("enter your password")
    if user_password=='quit':
        print("exit from the programme")
        break
    if user_password==password:
        print("successfully entered")
        break
    else:
        print("incorrect password")
    
'''
#Write a program that calculates the sum of the digits of a positive integer the user enters.
'''
x=int(input("enter a number:"))
sum1=0
while x>0:
    rem=x%10
    sum1+=rem
    x//=10
print("Sum of digits:", sum1)
'''
#Implement a program that calculates the result of raising a base number to an exponent entered by the user. Use a while loop to perform repeated multiplication
'''
number=int(input("enter a number:"))
exponent=int(input("enter a exponent value:"))
y=number
while exponent>1:
    y*=number
    exponent-=1
    
print(y)
'''
#Write a program to display factors of a positive integer entered by the user. Use a while loop to iterate over potential factors
'''
num=int(input("enter a number:"))
i=1
while i<=num:
    if num%i==0:
        print(i)
    i+=1
'''
#Write a Python program to sum up all the items in a list.
'''
x=[10,20,30,40]
total=0
for i in x:
    total+=i
print(total)
'''
'''
x=[11,22,33]
total=0
i=0
while i<len(x):
    total+=x[i]
    i+=1
print(total)
'''    
#condition statement workout pages
'''
if condition:#any statement,but the output should boolean
    statement
else:
    statement
'''
#finding biggest number from two numbers
'''
a=10
b=20
if a>b:
    print ("a is bigger number")
else:
    print("b is bigger number")
'''
#the age is greaterthan 18 print 'major',else print minor
"""
age=int(input("enter your age"))
if age>=18:
    print("major")
else:
    print("minor")
"""
# program to find out a number is odd/even:
"""
num=int(input("enter a number:"))
if num%2==0:
    print (f"{num} is an even number")
else:
    print(f"{num} is a odd number")
"""
'''
num=int(input("enter a number:"))
if num<=10:
    print("YELLOW")
elif num>10 and num<=20:
    print("BLUE")
else:
    print("BLACK")
'''
'''
letter=str(input("enter a letter:"))
if letter=="v" or letter=="V":
    print("violet")
elif letter=="i" or letter=="I":
    print("indigo")
elif letter=='b'or letter=='B':
    print("blue")
elif letter=='G' or letter=='g':
    print("green")
elif letter=='y' or letter=='Y':
    print("yellow")
elif letter=='o' or letter=='O':
    print("orange")
elif letter=='r' or letter=='R':
    print("red")
else:
    print("invalid")
'''
#find out the biggest number:
'''
num1=int(input("enter a number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if num1>num2 and num1>num3:
    print("num1 is greater number")
elif num2>num3 and num2>num1:
    print("num2 is greater number")
else:
    print("num3 is greater number")
'''
#loops:
#while loop:
#print hai 10 times:
'''
i=1
while i<=10:
    print("hai")
    i+=1
'''
#print 1-100
'''
i=1
while i<=100:
    print(i)
    i+=1
print("end")

'''
#break
'''
i=1
while i<=10:
    print(i,"hello")
    i+=1
    if i==5:
        break
'''
#continue:
'''
i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i)
'''
#checking a number is prime or not:
'''
num=int(input("enter a number:"))
i=2
while i<num-1:
    if num%i==0:
        print("its not a prime number")
        break
    i+=1
else:
    print("its a prime number")

'''
#inner loop concept:
"""
i=1
while i<=5:
    j=1
    while j<=3:
        print(i,j)
        j+=1
    i+=1
"""
#printing square pattern by using nested loop/inner loop:
'''
i=1
while i<=5:
    j=1
    while j<=5:
        print("*",end=" ")
        j+=1
    print()
    i+=1
    '''
#output
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''
#print a triangle showed :
"""
*
**
***
****
*****

i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1
"""
'''
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1
#output

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
#print a triangle showed below :
'''
      *
     * *
    * * *
   * * * *
  * * * * *

i=1
while i<=5:
    k=1
    while k<=(5-i):
        print(" ",end=" ")
        k+=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1
'''    
"""

i=5
while i>=0:
    print (" ",end=" ")
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i-=1
  * * * * * 
  * * * * 
  * * * 
  * * 
  * 
"""
#list:
'''
age=[20,45,12,75,45]
print(len(age))
print(age[-1])
age.append(24)
age.insert(2,60)
age.remove(12)#for removing element
age.pop()#for removing last element
age.pop(1)#for removing specific element by index number
print(age)
'''
#write a function that takes a list of numbers and returns a new list with each number squared:
'''
x=[1,2,3,4,5]
y=[]
def square():
    for i in x:
       a=i**2
       y.append(a)
    print(list(y))
square()
'''
#write a function to find the second largest element in a list:
'''
a=[5,3,2,4,9,7,2,1]
def scnd_large_element():
    a.sort()
    print(a[-2])
scnd_large_element()
'''
#write a function that removes duplicate elements from a list while preserving the order:
'''
list1=[9,5,3,1,2,4,3,5,6,8,9,7,2,3,5]
list2=[]
def duplicate_remove():
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
duplicate_remove()
'''   
























