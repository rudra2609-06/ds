import numpy as np

# a = np.array([[1,2,3],[4,5,6]])
# print(type(a))

# print(a)


# ------------ our own data type (dtype) ------------

# b = np.array([1,2,0],dtype=bool)
# b = np.array([1,2,0],dtype=float)
# print(b)

# ------------- np.arange ------------------

# print(np.arange(1,11)) #numpy array similar to range in python
# print(np.arange(1,11,2))  # also has step size

# ------------- np.reshape ------------------
# ensure total numbers equals to product of 2 numbers in reshape arguments	
# print(np.arange(1,11).reshape(2,5))

# ------------- np.ones and np.zeros and np.random ------------------

# print(np.ones((3,2))) #3 rows 2 cols all 1 requires tuple as input
# print(np.zeros((3,2)))

# print(np.random.random((3,4))) #gives random number from 0 to 1 in 3 rows 4 cols


# ------------- np.linspace ------------------

# generates equally seperated distanced points b/w given upper and lower range

# print(np.linspace(-10,10,10,dtype=int))
# -10 to 10 i want 10 numbers with linearly spaced

# ---------- np.identity -------------

# useful for creating identity matrix

# print(np.identity(3)) #3 by 3 identity matrix








