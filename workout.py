#type function
'''
a=12
b="rafeedha"
c=3.24
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''
#id()-used to find memory location of a variable
'''
a=3
b=12
c=3
print(a is b)
print(a is c)
print(id(a))
print(a is not b)
'''
#Write a program that calculates the factorial of a number using a while loop.
'''
num=int(input("enter a number"))
factorial = 1
i=1
while i<=num:
    factorial*=i
    i+=1
print(factorial)
'''
a=300
b=900
#print(a<=b)
print(a<b and a!=b)
print(a>b or a!=b)
