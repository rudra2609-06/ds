# set is a unordered collection of items in which all items are unique (no duplicates) and must be immutable (cannot be changed).

# Features:

# unordered
# mutable
# no duplicates
# can't contain mutable data types but set itself is mutable


# ---------- Creating set ----------

# *** empty set ***

# NOTE

# s1 = {}
# print(type(s1)) # -> dictionary as set and dictionary shares the same syntax if we try to create set with {} syntax we will find out that it is dictionary 

# s2 = set()
# print(type(s2))
# print(s2)


# s1 = {1,2,3,4}
# print(s1)

# we can't create 2d set as set inside set will be mutable 


# s2 = {1,2,True} #1 and True-> 1 therefore set contains unique elements only 1 value will be there

# print(s2)

# s4 = set([1,2,3])
# print(s4)


# ---------- Accessing elements set ----------

# there is not indexing in sets as they are unordered no slicing too

# ---------- editing set ----------

# as accessing elements are not possible we can't edit them

# ---------- adding elements set ----------

# add: adds one item at one time
# s1 = {1,2,3,4}
# s1.add(2)
# print(s1)

#update: adds multiple items at one time
# s1 = {1,2}
# s1.update([1,2,3,4])
# print(s1)


# ---------- deleting items set ----------

# s1 = {1,2,3}
# del s1
# print(s1)


# discard

# s1 = {1,2,3}
# s1.discard(2)
# s1.discard(50) #does not deletes the items and does not throw any error
# print(s1)


#remove : similar to discard if not found throws error
# s1 = {1,2,3}
# s1.remove(2)
# s1.remove(50) #error

#pop : randomly deletes any element
# s1 = {1,2,3}
# s1.pop()
# print(s1)

#clear : truncates the set clear all items in set

# s1 = {1,2,3}
# s1.clear()
# print(s1)





