#list methods
'''
x=[1,2,3,4,5]
x.append(5)
print(x)

x=[1, 2, 3, 4, 5, 5]
x.insert(4,6)
print(x)

x=[1, 2, 3, 4, 6, 5, 5]
x.remove(5)
print(x)
'''
x=[1, 2, 4, 3, 6, 5]
x.sort()
print (x)

x=[1, 2, 4, 3, 6, 5]
x.sort(reverse=True)
print (x)
'''
x=[6, 5, 4, 3, 2, 1]
x.reverse()
print(x)

x=[2,4,2,5,2,5,2,4]
print(x.count(2))


x=[2,4,2,5,3,2,5,2,4]
print(x.index(3))

x=[1,2,3]
y=[4,5,6]
y.extend(x)
print(y)

x=[2,4,2,5,3,2,5,2,4]
print(len(x))
'''
#for loop
'''
lists=[10,20,30,40,50]
i=0
while i<len(lists):
    print(lists[i])
    i+=1
print("end")

lists=[10,20,30,40,50]
for x in lists:
    print (x)
print("end")

for i in range(1,11):
    print(i)
print("end")

for i in range(11):
    print(i)
print("end")

for i in range(1,21,2):
    print(i)
print("end")

for i in range(0,21,2):
    print(i)
print("end")

for i in range(0,21):
    print(i,end="")
print("end")

x=[10,20,30,40,50]
for i in range(0,len(x)):
    print(x[i]
"""   
mark=[]
obtained_marks =60
while True:
    score=int(input("enter your subject score"))
    if obtained_marks==score:
        print(obtained_marks)
        break
    else:
        print(score)



'''
'''
marks=[]
for i in range(0,6):
    while True:
        mark= int(input("enter the mark"))
        marks.append(mark)
        print(marks)
        break
    else:
        print("invalid")
        
'''




