import numpy as np
import pandas as pd

# country = ['India','Usa','nepal','bhutan']

# series is 1d arrray in pandas it is similar to col in table

# s1 = pd.Series(country)
# print(s1)

# pandas if give dtype = 'str' it is actually 'object'

# marks = [67,88,99,100]
# sub = ['maths','science','hindi','ss']

# sub -> idx
# marks -> values

# s2 = pd.Series(marks,index=sub)


# ------------------- setting name -------------------

# s2 = pd.Series(marks,index=sub,name="Rudra Marks")
# print(s2)

# ------------------- using dict to create series -------------------

# marks = {
# 	'hindi':100,
# 	'sst' : 90,
# 	'maths':20
# }
 
# s3 = pd.Series(marks)
# print(s3)

# ------------------- Series Attributes -------------------

marks = {
	'hindi':100,
	'sst' : 90,
	'maths':20
}

my_marks = pd.Series(marks)

# ------------------- size -------------------
# print(my_marks.size)

# ------------------- dtype -------------------
# print(my_marks.dtype)

# ------------------- name -------------------
# print(my_marks.name) # if given then will return or else None

# ------------------- is_unique -------------------
# tells if our series all items are unique or not

# print(my_marks.is_unique) #True

# ------------------- index -------------------

# returns all index

print(my_marks.index)
# print(type(my_marks.index)) # Index class obj


# ------------------- values -------------------

# returns all values from series

# print(my_marks.values)
# print(type(my_marks.values)) #Numpy array




