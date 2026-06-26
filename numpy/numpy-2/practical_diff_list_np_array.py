import numpy as np

# numpy array better than python list: 1] Speed 2] Memory 3] Convenience

# ------- speed difference -----------

# import time

# a = [i for i in range(10000000)]
# b = [j for j in range(10000000,20000000)]

# start = time.time()

# c = []
# for i in range(len(a)):
# 	c.append(a[i] + b[i])

# print("Time Taken by python list: ",time.time() - start) #1.3


# a = np.arange(10000000)
# b = np.arange(10000000,20000000)
# start = time.time()
# c = a + b
# print("Time taken by numpy array: ",time.time() - start) #0.09


# ---------------- Memory Difference ----------------

# import sys

# a = [i for i in range(10000000)]
# print("Memory taken by python list(in bytes): ",sys.getsizeof(a))

# b = np.arange(10000000,dtype=np.int8)

# print("Memory taken by numpy array(in bytes): ",sys.getsizeof(b))

