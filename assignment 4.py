#task 01:
#question:1

year=int(input("enter a year:"))
if (year%4==0)and (year%100!=0)or (year%400==0):
    print("it is a leap year")
else:
    print("it is not a leap year")

#question:2

num=int(input("enter a number"))
if (num%5==0) and (num%7==0):
    print(f"{num} is factor of both 5 and 7")
else:
    print("it is not a factor of 5and 7")

#question:3

a=int(input("enter the 1st side length"))
b=int(input("enter the 2nd side length"))
c=int(input("enter the 3rd side length"))
if a+b>c :
    print("valid")
elif b+c>a:
    print("valid")
elif c+a>b:
    print("valid")
else:
    print("not a triangle")
    

#question:4

x=int(input("enter a number:"))
y=int(input("enter a number:"))
z=input("enter an operator")
if z=='+':
    print (x+y)
elif z=='-':
    print(x-y)
elif z=='*':
    print(x*y)
elif z=='/':
    print(x/y)
else:
    print("invalid")

#question:5

x=int(input("enter x value:"))
y=int(input("enter y value:"))
if x>0 and y>0:
    print("First Quadrant")
elif x<0 and y>0:
    print("Second Quadrant")
elif x<0 and y<0:
    print("Third Quadrant")
elif x>0 and y<0:
    print("Fourth Quadrant")
elif x==0 and y==0:
    print("Origin")
else:
    print("invalid")

#question:6

weight=float(input("enter the weight:"))
height=float(input("enter the height:"))
bmi=weight/height**2
print(bmi)
#BMI= W / H^2
if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<24.9:
    print("normal weight")
elif 25<=bmi<29.9:
    print("overweight")
elif bmi>=30:
    print("obesity")
else:
    print("invalid")

#question:7

age=int(input("enter your agae:"))
if age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("teenager")
elif age>=20 and age<=64:
    print("adult")
else:
    print("senior")

#question:8

day=int(input("enter a number"))
if day==1:
    print ("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif day==7:
    print("saturday")
else:
    print("invalid")

print("end")






    
