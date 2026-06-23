# attributes are similar to properties in javascript they are readonly so no calling ()

import numpy as np

a1 = np.arange(10)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# -------------- find out array dimension --------------
# ndim -> number of dimension

# print(a1.ndim)
# print(a2.ndim)
# print(a3.ndim)

# -------------- find our how many rows and cols -----------
# shape -> returns tuple 

# print(a1.shape) #1D array because tuple with one element 
# print(a2.shape) #(3,4) which means 3 rows 4 cols
# print(a3.shape) # (2,2,2) means there are 2 2d arrays of shape 2,2

# ------------------ gives number of items in array ------------
# print(a3.size)
# print(a1.size)

# ------------ each items occupies how many space in array ---------

# print(a2.itemsize)

# ------------- items data type -----------

# print(a1.dtype)
# print(a2.dtype)

# ------------ changing data types ----------


# print(a3.dtype) #int64

# a3.astype(np.int32)
# # creates a new array of type int32, but since you don't assign it to anything, that new array is discarded
# print(a3.dtype) #still int 64

# correct way
# a3 = a3.astype(np.int32)
# print(a3.dtype)
