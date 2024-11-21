#functions:
#without return
'''
def greet():
    print("hii")
    print("good morning")
greet()
'''
#with return keyword:
'''
def greet():
    return "good morning"
print (greet())
'''
'''
def greet(name):
    return f"{name}, good morning"
print (greet("Rafeedha"))

def greeting(name, place):
    return f"{name}, are you from {place}?"
print (greeting("rafeedha", "kondotty"))
print(greeting(place="kondotty",name="rafeedha"))
'''
'''
def add(num1, num2):
    return f"your numbers are {num1},{num2}"
print(add(10,20))
'''
#setting default parameter:
'''
def greet(name, place="kochi"):
    return f"hii {name}, are you from {place}?"
print(greet("rafeedha", "maalapuram"))
print(greet("safa"))
'''
'''
def add(*args):
    print(args)
    total=0
    for i in args:
        if type(i)==int or type(i) ==float:
            total+=i
    return total
print(add(1,2,3,4,5,6,7,7,"12","hello",3.15))
'''
#fibnacci sequence
#0,1,1,2,3,5,8,13,21
#normal
'''
x=0
y=1
print(x,end=",")
print(y,end=",")
for i in range (10):
    z=x+y
    print(z,end=",")
    x,y=y,z
'''    
#by using function:
'''
def fibinocci(num):
    x=0
    y=1
    print(x,end=",")
    print(y,end=",")
    for i in range (10):
        z=x+y
        print(z,end=",")
        x,y=y,z
    num=int(input("enter the limit"))
    print(fibinocci(num))
    
'''

















