#for loop in 2 lists:
"""
colors=["red","blue","black","green","white","yellow"]
traffic=["red","yellow","green"]
for i in colors:
    if i in traffic:
        print(f"{i} is in traffic")
    else:
        print(f"{i} not in traffic")
"""
#question (numbers[1,2,3,4,5],squares[],output=[1,4,9,16,25]
"""
numbers=[1,2,3,4,5]
squares=[]
for x in numbers:
    squares.append(x**2)
print(squares)
"""
#question(colors["red","yellow","orange","white","green"],output=red-stop, green -go, )
"""
colors=["red","yellow","orange","white","green"]
for x in colors:
    if x=="red":
        print("stop")
    elif x=="green":
        print("go")
    else:
        print(x)
    
"""
#question("red","blue","green"),number[1,2,3,4,5],output(red1,blue2,green3)
"""
colors=["red","blue","green"]
numbers=[1,2,3,4,5]
for i in colors:
    for x in numbers:
        print(i,x)
"""
"""
colors=["red","blue","green"]
numbers=[1,2,3,4,5]
for x in numbers:
    for i in colors:
        print (x,i)
"""
"""
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
#output
    # *
      **
      ***
      ****
      *****
"""
"""
for i in range (5):
    for j in range(5-i):
        print("*",end=" ")
    print()
#output
    #*****
     ****
     ***
     **
     *
"""
"""
for i in range(4):
    for j in range(3-i):
        print(" ",end=" ")
    for x in range(i+1):
            print ("*",end=" ")
    print()

#output
       *
      **
     ***
    ****
"""
'''
for i in range(5):
    for j in range(5-i):
        print(" ",end=" ")
    for y in range(2* i-1):
        print("*",end=" ")
    print()
'''
'''
#output
    *
   ***
  *****
 *******
'''
'''
for x in range(6):
    for y in range(x+1):
        print(" ",end=" ")
    for z in range(6-x):
        print("*",end=" ")
    print()
#output
    ******
     *****
      ****
       ***
        **
         *
'''

for i in range(5):
    for r in range (i-1):
        print(" ",end=" ")
    for n in range(5-i):
        print("*",end=" ")
    print()













