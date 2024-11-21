#01
'''
for i in range(1,101):
    i+=1
    if i%5==0:
        continue
    elif i%2==0:
        print(i)

#02

num=int(input("enter a number:"))
total=0
i=1
while i<=num:
    if i%2==0:
        total+=i
    i+=1
print(total)
'''
#3-incomplete
for i in range(5):
    for j in range (i+1):
        print(5-j,end=" ")
    print()

#04-incomplete
'''
num=int(input("enter a number:"))
i=1
while i<=num:
    fact=num%i==0
    if fact
        if
        print (i)
    i+=1
    
#07

str1="banana"
print(str1.count("n"))
print(str1.count("a"))
print(str1.count("b"))

#08

dict1={
    'x':10,
    'y':20,
    'z':30
    }
dict2={}
for i,j in dict1.items():
    if j in dict2:
        dict2[j].append[i]
    else:
        dict2[j]=[i]
print(dict2)

#10

sample_list=['hello','world','python']
x="".join(sample_list)
print(x)

#14

num=(input("enter a numbe:"))
if num==num[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

#09

dict1={
    'data1':5,
    'data2':3,
    'data3':2
    }
product=1
print(dict1.values())
for i in dict1.values():
    product*=i
print(product)

#11

original_list=[7,2,9,4,1]
original_list.sort()
print(original_list)
second_smallest_element=original_list[1]
print(original_list[1])

#15

list1=[1,2,3]
list2=[2,3,4]
set1=set(list1)
set2=set(list2)
print(set1)
print(set2)
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
'''
#16

for i in range (5):
    for j in range(i+1):
        print(i*2+1,end=" ")
    print()















