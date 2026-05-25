'''
Python list stores references to objects, not the actual values directly.

The list keeps memory addresses of objects like integers, strings or booleans.
Actual objects exist separately in memory.
Modifying a mutable object inside a list changes the original object.
Reassigning an immutable object creates a new object instead of changing the old one.

Drawbacks of list:
takes more time than array in other languages
takes more memory space than array in other languages
'''

# -------- creating list --------

# method 1
l0 = [1,2,'rudra',[1,2,3]]
l1 = [1,2,3]
# print(id(l1))
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l1[2]))
# print(id(1))
# print(id(2))
# print(id(3))



# method 2
l2 = list("rudra")
l3 = list((1,2,3))
# print(l2)
# print(l3)


# method 3
l4 = [5] *4
# print(l4)

# -------- accessing elements in list --------

l5 = [1,2,3,[4,5]]

# print(l5[-1])
# print(l5[-2])

# l6 = [[[1,2],[3,4],[5,6]]]

# if i want to remove 4 from [4,5]
# print(l5[3][0])
# print(l5[-1][-2])
# print(l6[0][0][0]) #from 3d or 2d array same process followed

# slicing
# print(l5[0:3])
# print(l5[0::2])


# -------- adding item in list --------

# append always try to add element at the end of the list as "single item" even if we try to append multiple items it will add it as single item

L = [1,2,3]

# L.append([4,5,6]) 
# print(L)
#list now will not be [1,2,3,4,5,6] instead append will try to add [4,5,6] as single item as now list will be [1,2,3,[4,5,6]]

#extend always try to break the multiple elments and then add into existing list

# L.extend('delhi')
# print(L)
#in this case extend will extend 'delhi' into 'd','e','l','h','i' and then add into existing list now list will be [1,2,3,'d','e','l','h','i']

# insert: if you want to add element at desired index than just pass the desired index and value in insert function

# L.insert(1,100)
# L.insert(1,[0,0]) #this will add a single value
# print(L)

'''
Summary:

append()
Adds one object at the end of the list.

extend()
Takes an iterable (list, tuple, string, etc.) and adds each element separately.


insert()
Adds one object at a specific index.
'''

# -------- editing item in list --------

# L1 = [1,2,3,4]
# L1[-1] = 250
# L1[0] = 100

# instead of 2,3,4 i want 200,300,400
# L1[1:4] = [200,300,400]
# print(L1)

# -------- deleting item in list --------

# del
L3 = [1,2,3,4]

# del L3[-2:-4]
# print(L3)
# del L3
# del L3[-1]
# del L3[-1:-2]

# remove(val): Removes the first occurrence of an element.

# L3.remove(2)
# print(L3)

# pop() Removes the element at a specific index or the last element if no index is specified.
# L3.pop()
# print(L3)

# L3.pop(0)
# L3.pop(-1)
# L3.pop(0:2) error
print(L3)

# clear():removes all items. similar to truncate in sql only [] will be left behind




