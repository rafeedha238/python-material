#in this while loop the 1 may show infinite
'''
i=1
while i<=10:
    print(i)
'''
"""
i=1
while i<=10:
    print(i) 
    i+=1
print("the end")
"""
"""
i=1
while i<=5:
    print(i)
    i+=1
print("end")
"""
"""
num= int(input("enter the number"))
i=1
while i<=10:
    print(f"{i}*{num}={i*num}")
    i+=1
print("end of program")
"""

#1-100 find out 5, 3 multiplications
"""
i=1
while i<=100:
    print (i)
    i+=1
print("end")
"""      
"""
i=1
while i<=100:
    if i%5==0 and i%3==0:
        print(i)
    i+=1
print("end")
"""
"""
i=1
while i<=100:
    if i%3==0:
        print("fizz")
    elif i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
    i+=1
"""
'''
i=1
while i<=100:
    if  i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
    i+=1

'''
# break (control statement)
"""
i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1
print("end")
"""
#continue statement:
#while true(refer), list
# find out the odd and even numbers in between 1-20:(hom)
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1
print ("end program")

i=1
while i<=20:
    if i%2!=0:
        print(i)
    i+=1
print("end")

