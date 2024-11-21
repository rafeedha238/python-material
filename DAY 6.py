"""
password= "text@123"
while True:
    user_password= input("enter your password")
    if password==user_password:
        print("successfully logged in")
        break
    else:
        print("try again")
    
"""
sample= [20,45,30,25,35,10]
"""
print(len(sample))
print(sample)
print(sample[1::2])
"""     
print(sample[::2])
print(sample[-5:])
print(sample[-5:-2])
print(sample[-5::1])
print(sample[::-1])
print(sample[-1:])
print(sample[::-2])
sample.append(76)
print(sample)
