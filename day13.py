#join():
'''
converting a list into string
'''
#strip()
'''
for removing charactors in starting point and ending point
'''
x="##hello##"
print(x.strip("#"))#for removing the start and end characters


x="##hello##"
print(x.lstrip("#"))#for removing the left characters

x="##hello##"
print(x.rstrip("#"))#for removing the right characters

#split lines
'''
Splits the string at line breaks and returns a list
'''
'''
eg:
"""welcome to
   python, it is
   programming language"""
add - "python is easy to read and write"
'''
x="""welcome to
   python, it is
   programming language"""
y=x.split()
print(y)
