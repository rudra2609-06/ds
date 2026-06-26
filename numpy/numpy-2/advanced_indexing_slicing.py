import numpy as np
# a = np.arange(24).reshape(4,6)

# Fancy Indexing

# if want 1st,3rd and 4th row

# print(a[[0,2,3]])

# if i want 1st col , 3rd col and 4th col

# print(a[:,[0,2,3]])

# ----------- Boolean Indexing -------------

# range -> 1 to 100
# size -> 24
b = np.random.randint(1,100,24).reshape(6,4)
print(b)

# find all numbers greater than 50

# b > 50 #boolean array
# print(b[b > 50]) #masking with original array to get values from boolean array

# find all even numbers

# print(b[b % 2 == 0])

# find all numbers greater than 50 "and" are even

# print((b > 50) & (b % 2 == 0))
# print(b[(b > 50) & (b % 2 == 0)])

# find all numbers not divisible by 7

# print(b[b % 7 != 0])
# ---------- OR ----------
# print((b[~(b % 7 == 0)]))







