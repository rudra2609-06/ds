'''
Advantages of list comprehension:
More time and space efficient than loops
Completes the tast in single line
Transform loop into one formula

newList = [expression for item in iterable if condition == True]
'''

# List comprehension is a concise way to create new lists by applying an expression to each item in an existing iterable like a list, tuple or range. It helps to write clean, readable and efficient code compared to traditional loops.

# a = [1,2,3,4]
# print(a)
# b = [val ** 2 for val in a]
# print(b)

# Conditional Statements in List Comprehension

a = [1,2,3,4]
# b = [val for val in a if val % 2 == 0]
# print(b)

# c = [val for val in a if val > 2]
# print(c)

# --------- problems ---------

# add 1 to 10 numbers into empty list

n1 = []
for i in range(1,11):
	n1.append(i)

# print(n1)

# instead we can do

n2 = [val for val in range(1,11)]
# print(n2)

# scalar multiplication of vector 

# v = [1,2,3]
# s = 3

# n3 = [val * s for val in v]
# print(n3)

# print all numbers divisible by 5 in range of 1 to 50

n4 = [val for val in range(1,51) if val % 5 == 0]
# print(n4)

# find a language which start with letter p

n5 = ['php','javascript','python','java','cpp']

# n6 = [val for val in n5 if val.startswith('p')]
# print(n6)

# nested if with list comprehension

basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','graps','banana']

# create a newlist such that it contains elements similar to basket and also starts with letter 'a'

n7 = [val for val in my_fruits if val in basket and val.startswith('a')]
print(n7)

# cartesian products

n8 = [1,2,3,4]
n9 = [5,6,7,8]

n10 = [(x,y) for x in n8  for y in n9]
print(n10)
