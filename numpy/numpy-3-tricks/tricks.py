import numpy as np

# -------------------------------- np.sort(array) --------------------------------

# returns sorted "numpy array"

# -------------- 1D Case --------------

# a = np.random.randint(1,100,15)
# a_sorted = np.sort(a) #by default ascending
# a_sorted = np.sort(a)[::-1] #descending
# print(a_sorted)

# -------------- 2D Case --------------

# b = np.random.randint(1,17,16).reshape(4,4)

# b_sorted = np.sort(b)
# print(b)
# print(b_sorted) #default sorts row wise (axis 1)
# print(np.sort(b,axis=0)) #sort column wise (axis 0)


# -------------------------------- np.append(array) -------------------------

# np.append(array) appends values along the mentioned axis at the end of the array

# c = np.arange(1,21)

# # c = np.append(c,200)
# # print(c)



# d = np.arange(1,21).reshape(4,5)

# # add col after 1st row's end
# # print(d.shape)

# # d = np.append(d,np.ones((d.shape[0],1)),axis=1)
# # print(d)


# ----------------------------- np.concatenate(tuple containing arrs) ---------------

# concatenate sequence of arrays along the specific axis

# a = np.arange(6).reshape(2,3)
# b = np.arange(6,12).reshape(2,3)

# print(a)
# print(b)

 
# c = np.concatenate((a,b),axis=0)
# c = np.concatenate((a,b),axis=1)
# print(c)

# ----------------------------- np.unique(array) ----------------------------

# returns unique elements from an array
# axis = 0 -> means consider each row as 1 item
# axis = 1 -> means consider each col as 1 item

# e = np.array([1,1,1,2,2,3,3,4,4,5,5])
# f = np.array([[1,2,3,1],[1,2,3,2]])

# print(e)
# print(f)

# print(np.unique(e)) # [1,2,3,4,5]
# print(np.unique(f)) #[1,2,3]


# -------- expand_dims --------

# a = np.arange(1,11)
# print(a.shape)
# b = np.expand_dims(a,axis=1)
# print(b.shape)
# b = np.expand_dims(a,axis=0)
# print(b.shape)


# ------------------------ np.where() ----------------

# np.where(condition,if true what to do,if false what to do)

# returns idx of element where given condition is satisfied
# returns all idx in tuple
# a = np.random.randint(1,100,15)

# idx of all elements whose value is greater that 50

# indexes = np.where(a > 50)
# print(indexes)

# replace all elements whose value is greater that 50 to 0

# a[np.where(a > 50)] = 0

# a > 50 if it is true that replace it with 0 else replace it with particular number
# a = np.where(a > 50,0,a)
# print(a)




