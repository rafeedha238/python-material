#1
'''
student_marks={
    "anand":65,
    "abinand":75,
    "athul":81,
    "benison":42,
    "hafeed":35,
    "jithin":95,
    }
student_grade={}

for i,j in student_marks.items():
    #print(student_marks[i])#get all the values
    print(student_marks.get(i))#this also used to get all values
    if j>90:dict2[j]
        student_grade[i]="a+"
    elif j>81:
        student_grade[i]="a"
    elif j>70:
        student_grade[i]="b+"
    elif j>60:
        student_grade[i]="b"
    elif j>50:
        student_grade[i]="c"
    elif j>40:
        student_grade[i]="d"
    else:
        student_grade[i]="f"
print(student_grade)

 '''
#string methods
#checking whether a string is palindrome or not
'''
text=input("enter a string:")
if text==text[::-1]:
    print("it is a palindrome")
else:
    print("not a palindrom")
'''
'''
x="python world"
print(x.capitalize())
print(x.title())#capitalize the first letter of each word
print(x.upper())#converting the word into capital letters
print(x.lower())#converting the word into lower case
print(x.count("o"))#the count of specific value in a sentence
print(x.find("o"))#to findout the index position
print(x.endswith("thon"))#Returns true if the string ends with the specified value
print(x.startswith("py"))#Returns true if the string starts with the specified value
'''


#converting the string into list
'''
y="python learning on progress"
x=y.split()
print(x)
'''
#spliting a sentence by using a letter
'''
y="python learning on progress"
x=y.split("n")
print(x)
'''
#converting a list into string(without space)
'''
y=["python","learning"]
x="".join(y)
print(x)
'''
#converting a list into string(without space)
'''
y=["python","learning"]
x=" ".join(y)
print(x)
'''
























        
        
    
