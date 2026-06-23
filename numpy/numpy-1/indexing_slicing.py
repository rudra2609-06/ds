import numpy as np


a1 = np.arange(10)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)


# print(a1[-1])

# print 6 from a2
# print(a2)
# print(a2[1][2])
# print(a2[1,2])


# print 5 from a3
# print(a3)
# print(a3[1,0,1])



# ------------------ slicing -----------------
# remember in slicing case within 1d we generally consider second argument after : to be exluding but in above 1d it is not like that second arguement is including


# print(a1)
# 2,3,4
# print(a1[2:5])


# print(a2)
# # first row and all cols
# print(a2[0f])

# # first col
# print(a2[:,0])

# 5,6 and 9,10
# print(a2[1,[1,2]])
# print(a2[2,[1,2]])

# i want numbers from 2,3rd row so therefore 1 onwards
# print(a2[1:,1:3])


# 0,3,8,11
# in rows i want jump of 1 and in col i want jump of 2 that's why +1 always as it is excluding in this type of syntax not similar to 1d slicing
# print(a2[::2,::3])

# 1,3,9,11

# print(a2[::2,1::2])

# 4,7
# print(a2[1,::3])

# 1,2,3,5,6,7

# print(a2[:2,1::])


# print(a3)
# this consists of 3 2d arrays

# matrix/2d array with index 1
# print(a3[1])

# 1st matrix and last matrix
# print(a3[::2])

# 1st matrix's 2nd row : [3,4,5]
# print(a3[0,1,:])

# 2nd matrix's mid col elements: [10,13,16]

# print(a3[1,:,1])

# 0,2,18,20
# print(a3[::2,0,::2])


# ------- iterating -------

# over 1d array
# for i in a1:
# 	print(i)

# over 2d array: it prints one row at a time
# for i in a2:
# 	print(i)

# over 3d array: it prints matrix/2d array at a time
# for i in a3:
# 	print(i)

# if you want to print all elements

# for i in np.nditer(a3):
# 	print(i)


# ----------- Reshaping -------------

# reshape : already covered

# transpose : rows-> col col -> rows

# print(a2)
# print(a2.transpose())
# print(a2.T) # --------- OR ---------


# ravel : converts ndimenstion array to 1d array

# print(a3.ravel())

# -------------- Stacking: takes tuple as input data type ---------------

# horizontal stacking

a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

# print(np.hstack((a4,a5)))

# vertical stacking

# print(np.vstack((a4,a5)))



# -------------- Splitting  ---------------

# horizontal splitting: array and how many equal parts

# print(np.hsplit(a4,2))

# vertical splitting: array and how many equal parts

# print(a4)	
# print(np.vsplit(a4,3))

