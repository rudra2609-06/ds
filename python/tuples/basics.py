# tuples are similar to list but only thing is that they are immutable. Once elements added in tuple we can't change them unlike list

#tuples are used mostly in readonly-applications

# features of tuples:

# ordered
# duplicates allowed
# immutable
#faster than list
#takes less memory than list

# -------- Creating Tuples --------

# empty tuple
t1 = ()
# print(t1) # ()

# *** creating tuple with single item ***

t2 = (1)
# print(t2) #1
# print(type(t2)) #<class 'int'>

t3 = ('hello')
# print(t3) # 'hello'
# print(type(t3)) # <class 'str'>

t4 = ('hello',)
# print(t4) # ('hello',)
# print(type(t4)) # <class 'tuple'>

# it creates a problem when creating tuple with one item so we need to add a comma when creating tuple with one item else it will create int or str or float respectively

# homo
t5 = (1,2,3,4)
# print(t5) #(1,2,3,4)

#hetero
t6 = (1,2,3,4,'hello',True)
# print(t6) # (1,2,3,4,'hello',True)

#2D tuple
t7 = (1,2,3,(4,5))
# print(t7) #(1, 2, 3, (4, 5))

#type conversion

t8 = tuple((1,2,3))
# print(t8)


# -------- Accessing items Tuples --------

t9 = [1,2,3,4]

# indexing

# print(t9[0])
# print(t9[-1])
# print(t9[::-1])

# slicing

# print(t9[0:3])

# -------- Editing items Tuples --------

# they are immutable we can't edit them

# -------- adding items Tuples --------

# adding is also editing something we can't add them after creation

# -------- deleting items Tuples --------

# similarly if we want to delete whole portion of tuple we can do that but if we want to remove a portion we can't do that

# t10 = (1,2,3,4)
# del t10
# del t10[0:2] #error we can't do that
# print(t10) #error tuple deleted




