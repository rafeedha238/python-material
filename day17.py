#exception handling eg:
'''
print("start")
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a/b)
except ValueError:
    print("enter a integer number")
finally:
    print("end")
'''
#decorator:
'''
def decorator(greeting):
    def wrap():
        print("****")
        greeting()
        print("****")
    return wrap
@decorator
def greet():
    print("hello, good morning")
greet()
'''
#python modules:
#how to access data from modules:
'''
import math
help(math)

import math
print(math.pi)

import math as m
print(m.pi)

from math import pi,floor,ceil
print(pi)
print(floor(4.69))
print(ceil(5.78))

from math import *
print(pi)
print(sqrt(25))
print(factorial(5))

import random
help(random)

from random import *
print (random())
print(randint(1000,9999))
print(choice(["a","b","c"]))
'''
import datetime
help(datetime)


import string
help(string)
















