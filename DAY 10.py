'''
tuple()
-one and more datas handling
- inchangable(immutable)
- ordered
- indexing and negative indexing
- slicing
- duplicates are allowed

*methods
1.count
2.index
eg:
x=(1,2,"hello",True)
print(x[0])
output= 1

eg:
'''
'''
numbers=(1,2,3,4,5)
print(numbers)
print(type(numbers))#type casting
print(numbers[0])#first position
print(numbers[-1])#last position
print(numbers[::-1])#slicing
'''
#adding to tuples
'''
x=(1,2,3)
y=(4,5,6)
print(x+y)
'''
#coverting tuple into list

'''
x=(1,2,3,4)
y=list(x)
y.append(5)
x=tuple(y)
print(x)
'''

#list in a tuple
'''
x=(1,True,3.14,"hello",[1,2,3,4])
print(x)
print(x[-1])
x[-1].append(6)
print(x)
'''
'''
x=(1,True,3.14,"hello",[1,2,3,4])
print(x[4][2])
'''
'''
x=[1,2,3,[4,5,6,[7,8,9,[10,11],12],13],14,15,[16,17],18]
print(x[3][1])
print(x[3][3][2])
print(x[3][3][3][0])
print(x[3][4])
print(x[6][1])
'''
#set{}
'''
-unordered
-all elements are unique
-changable
'''
#set methods
'''
1) add()= To add one item to a set use the add() method.
2) remove()=To remove an item in a set
3) discard()= If the item to remove does not exist, discard() will NOT raise an error.
4) pop()=	Removes an element from the set
5) clear()= Removes all the elements from the set
6) len()= findout length
7) union()= Return a set containing the union of sets
8) update()= Update the set with the union of this set and others
9) difference()= Returns a set containing the difference between two or more sets
10) difference_update()= Removes the items in this set that are also included in another, specified set
11) symmetric_difference()= Returns a set with the symmetric differences of two sets
12) symmetric_difference_update()= Inserts the symmetric differences from this set and another
13) issubset()= Returns whether another set contains this set or not
14) issuperset()= Returns whether this set contains another set or not
15) intersection()= Returns a set, that is the intersection of two other sets(coomon areas of 2 sets)
16) intersection_update()= Removes the items in this set that are not present in other, specified set(s)
17) isdisjoint()= Returns whether two sets have a intersection or not
'''
#setA={1,2,3,4,5}
#setB={4,5,6,7,8}
#print(setA.union(setB))
#setA.update(setB)
#print(setA)
#print(setA.intersection(setB))
#setA.intersection_update(setB)
#print(setA)

#print(setB.difference(setA))
#setB.difference_update(setA)
#print(setB)

#print(setA.symmetric_difference(setB))
#setA.symmetric_difference_update(setB)
#print(setA)
a={1,2,3,4}
b={3,4}
c={9,10}
d={3,8}
#print(a.issuperset(b))
#print(a.issubset(c))
print(a.isdisjoint(d))
print(a.issubset(d))



