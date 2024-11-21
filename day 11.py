#removing duplication from a list
'''
x=[5,2,1,2,3,4,2]
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)

'''
#removing duplication from a list by using set
'''
x=[5,2,1,2,3,4,2]
y=set(x)
print(y)
'''
#dictionary:
'''
-{} braces are used in dict
-key value pair
-unique key
-changeble
-ordered
'''
#get():
'''
for getting items indict
eg:
    print(phone_numbers.get("athul")
#update():adding a new item
eg:-
    phone_number.update("beniso":"0999")
    print(phone_numbers)
'''
'''
roll_number={
    1:"abi",
    2:"baby",
    3:"cham",
    4:"dod"
    }
print(roll_number)
roll_number.pop(2)#pop the key item
print (roll_number)
roll_number.popitem()#to remove last item
print(roll_number)
roll_number.clear()#to clear all items
print(roll_number)
    
print(roll_number.keys())#for accessing keys only
print(roll_number.values())#for accessing values only
print(roll_number.items())#for accssing seperate tuples of a dic

for i in roll_number:
    print(i)

for i in roll_number:
    print(roll_number[i])

    #or
for i in roll_number.values():
    print(i)
    

for i in roll_number.items():
    print(i)

for i, j in roll_number.items():
    print(i,j)

print(len(roll_number))
'''
#zip():
#compaigning 2 lists for converting to dictionary
x=["physics","chemustry","maths"]
y=[40,30,20]
sample=list(zip(x,y))
print(sample)
sample_dict=dict(zip(x,y))
print(sample_dict)














