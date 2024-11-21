#read operator:
'''
file=open("sample.txt","r")
#print (file.read())
#print(file.read(8))
data=file.readlines()
print(data)
'''
#wirte:
'''
file=open("sample1.txt","w")
file.write("hello codeme")
file.write("sample data created")
file.close()
'''
#another method to file operator:
'''
with open("sample2.txt","w")as file:
    print(file.write("sample"))
    file.writelines(["\n see you","soon"])
'''
#append:
'''
file=open("sample.txt","a")
file.write("sample created")
file.close()
'''
#class , object:
class Watch():
    def __init__(self,brand,strap,waterproof,type):
        #properties
        self.brand=brand
        self.strap=strap
        self.waterproof=waterproof
        self.type=type
        self.time="12:00"
    def display(self):
        print(f"current time:{self.time}")
    def adjust_time(self,newtime):
        self.time=newtime
        print(f"adjusted time:{self.time}")
    def is_waterproof(self):
        '''
        if self.waterproof==True:
            print("waterproof")
        else:
            print("not")
        '''
        print(self.waterproof)
#object creation:
obj1=Watch("rolex","metal","False","analog")
obj2=Watch("fastrack","rubber","True","digital")
#object function accesing:
obj1.display()
obj2.display()
obj1.adjust_time("1:00")
obj1.is_waterproof()

        
    
