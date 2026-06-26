# Term broadcasting says how numpy treats arrays with different shapes while performing arithmetic operations
# The smaller array is broadcasted into larger array so they have compatible shapes


import numpy as np

# same shape

# a = np.arange(6).reshape(2,3)
# b = np.arange(6,12).reshape(2,3)

# print(a)
# print(b)

# print(a + b)


# different shape

# a = np.arange(3).reshape(1,3)
# b = np.arange(6).reshape(2,3)

# print(a)
# print()
# print(b)
# print()
# print(a + b)

# ------------- Broadcasting Rules -------------

'''
1] Make Sure that both array's should have same dimensions
-> If not, numpy will make sure that it will add one additional array to the head of smaller array until dimension are not equal

Eg:

(3,2) (3,) -> (3,2) (H,3) -> (3,2) (1,3) 1 is added to head
(3,3,3) (3,) -> (3,3,3) (1,1,3)

2] Make each dimension of two array's of same size
(2,3) (1,3) -> (2,3) (2,3)
'''

# a = np.arange(12).reshape(4,3)
# b = np.arange(3)

# print(a)
# print()
# print(b)
# print()

'''
a = (4,3) b = (3,)
a = (4,3) b = (1,3) [we made dimensions same]
a = (4,3) b = (4,3) [we made each dimesion of array same]
'''

# a = np.arange(12).reshape(3,4)
# print(a)
# b = np.arange(3)
# print(b)

'''
a = (3,4) b = (3,)
a = (3,4) b = (1,3) [we made dimensions same]
a = (3,4) b = (3,3) [we can't make each dimension of array same]
'''
# in this we can't do broadcasting 
