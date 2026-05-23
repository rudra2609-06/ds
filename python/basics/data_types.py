'''
data types in python:
Numeric: Integer,Complex Number,Float
Dictionary
Boolean
Set
Sequence Type: String,List,Tuple
'''

a = 5;
b = 3.3;
c = 2 + 3j;

print(type(a))
print(type(b))
print(type(c))

'''
output will be:
<class 'int'>
<class 'float'>
<class 'complex'>
therefore in python everything is treated as an object
'''

name = 'rudra'
print(type(name))
print(name[-1]);

# Lists are ordered and "mutable" collections used to store multiple items in a single variable
# list are ordered in a sense that they store values at particular indexes unlike set we can access value by []
a = [1,2,True]
a[2] = False
print(a[2])

# Tuples are ordered and immutable collections used to store multiple items in a single variable

t1 = (1,2,True)
#-------- OR --------
t2 = 1,2,True
# t2[2] = False ---> it will throw error as tuples are immutable
print("t2's 2:",t2[2])
print(type(t1))
print(type(t2))
print(type(t1[2]))
print(type(t1[1]))
