import numpy as np
import matplotlib.pyplot as plt

# ----------------------- np.argmax() -----------------------


# returns the indexes of max element in an array

# in 1d same case

# a = np.arange(1,50)
# print(a)
# print(np.argmax(a))

# in 2d same case
# a = np.arange(15).reshape(3,5)

# print(a)
# max element idx from each row
# print(np.argmax(a,axis=1))

# max element idx from each col
# print(np.argmax(a,axis=0))

# similar for min idx fn i.e. np.argmin(arr,axis)

# -------------------- np.cumsum() ---------------------

# if calculates cumulative sum for the given array

# a = np.array([1,2,3,4,5,6,7,8,9])

# print(np.cumsum(a))

# similar for 2d array by specifying axis


# -------------------- np.cumprod() ---------------------

# a = np.array([1,2,3,4,5,6,7,8,9])
# print(np.cumprod(a))


# ----------------- np.percentile() -----------------

# calculates n-th percentile of given data
# np.percentile(b, 100) #gives the maximum value in the array.
# np.percentile(b, 0) #gives the minimum value.

'''
what percentile actually means
percentile(b, 0)   → 0% of values fall below this  → minimum
percentile(b, 25)  → 25% of values fall below this → Q1
percentile(b, 50)  → 50% of values fall below this → median
percentile(b, 75)  → 75% of values fall below this → Q3
percentile(b, 100) → 100% of values fall below this → maximum

'''

# b = np.random.randint(1,17,16)

# print(np.percentile(b,100))
# print(np.percentile(b,0))

# ----------------- np.histogram() -----------------

# b = np.random.randint(1,17,16)

# # bins are step size 0-10,10-20,30-40
# histo = np.histogram(b,bins=[0,10,20,30,40,50,60])
# print(histo)
# plt.hist(histo)
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()



# -------------- np.corrcoef() --------------

# 0 -> means 2 variables are independent they are not dependent
# 1 -> means they are co-related 
# -1 -> inversly related one increases other decreases

salary = np.array([1000,2000,3000,4000,5000])
exp = np.array([1,3,4,5,7])

print(np.corrcoef(salary,exp))

'''
		salary      exp
salary [[1.0,        0.989]
exp     [0.989,      1.0  ]]

Why diagonal is always 1.0?
salary vs salary → perfectly correlated with itself → 1.0
exp vs exp       → same → 1.0
'''






