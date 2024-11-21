#palindrome:
'''
def palindrome(word):
    if word==word[::-1]:
        return"its a palindrome"
    else:
        return"its not a palindrome"
word=input("enter a word:")
print(palindrome(word))
'''
#lambda functions:
'''
sample=lambda :"hello"
print(sample())

text= lambda x: f"hii {x}, how are you"
print(text("rafeedha"))

add=lambda x,y: x+y
print(add(15,17))
'''
#map:

number=[1,2,3,4,5]
squares=map(lambda x: x**2,number)
print(squares)
print (list(squares))

'''
number=[1,2,3,4,5]
squares= map(lambda x: x**2 if x%2==0 else x, number)
print(list(squares))
'''
#filter
'''
number=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x: x%2==0,number)
print(list(even))
'''
#reduce:
'''
from functools import reduce
numbers= [1,2,3,4,5]
sum= reduce(lambda x,y:x+y, numbers)
print(sum)
'''
#list comprehension
#normally findout square
'''
numbers=[1,2,3,4,5]
square=[]
for i in numbers:
    square.append(i**2)
print(square)
'''
#findout square by using list comprehension
'''
numbers=[1,2,3,4,5,6]
squares=[i**2 for i in numbers]
print(squares)
'''
#1double the even numbers in a list
'''7
x=[1,2,3,4,5,6,7,8,9,10]
doubles=[]
for i in x:
    if i%2==0:
        doubles.append(i*2)
print(doubles)
'''
#by using list comprehension:
'''
x=[1,2,3,4,5,6,7,8,9,10]
doubles=[i*2 for i in x if i%2==0]
print(doubles)
'''

#2printing initials of names:
'''
name=["Alice","Benison","hafeed","sebin"]
initials=[]
for i in name:
    initials.append(i[0])
print(initials)
'''
#by using list comprehension:
'''
name=["Alice","Benison","hafeed","sebin"]
initials=[i[0] for i in name]
print(initials)
'''
#3prepare list of words with a in given list:
'''

words=["apple","banana","kiwi","cherry"]
words_with_a=[]
for i in words:
    if "a" in i:
        words_with_a.append(i)
print(words_with_a)
'''
#by using list comprehension:
'''
words=["apple","banana","kiwi","cherry"]
words_with_a=[i for i in words if "a" in i]
print(words_with_a)
'''
#4square the even numbers and cube the odd ones:
'''
number=[1,2,3,4,5]
square_cubes=[]
for i in number:
    if i%2==0:
        square_cubes.append(i**2)
    else:
        square_cubes.append(i**3)
print(square_cubes)
'''
#by using list comprehension:
'''
number=[1,2,3,4,5]
square_cubes=[i**2 if i%2==0 else i**3 for i in number]
print(square_cubes)
'''
#5print the numbers which are even and divisiblr by 3 in range of 20:
'''
for i in range(1,21):
    if i%2==0 and i%3==0:
        print(i)
    
'''
#by using list comprehension:
'''
even_divi=[i for i in range(1,21) if i%2==0 and i%3==0]
print(even_divi)
'''    




















