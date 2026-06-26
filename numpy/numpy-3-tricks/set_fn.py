import numpy as np


m = np.array([1,2,3,4,5])
n = np.array([6,7,8,9,10])

# print(np.union1d(m,n))
# print(np.intersect1d(m,n))
# print(np.setdiff1d(m,n)) #all those items in 1st set and not in second
# print(np.setxor1d(m,n)) #keeps all uncommon ones


a = np.random.randint(1,100,15)

# print(a)
# # now if we want all values to be clipped in range of 25 to 75
# print(np.clip(a,a_min=25,a_max=75)) #all values greater that 75 will become 75 and all values lesser than 25 will become 25
