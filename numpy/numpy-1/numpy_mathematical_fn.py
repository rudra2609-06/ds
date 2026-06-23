import numpy as np

a1 = np.arange(1,10).reshape(3,3)


# max_min_sum_product

# print(np.max(a1))
# print(np.min(a1))
# print(np.sum(a1))
# print(np.prod(a1))

# maximum/minimum/sum/product from each row or each col
# 0 -> col 1 -> row
# print(a1)
# print(np.max(a1,axis=1))


# -------- statistics fn --------

# print(np.mean(a1))
# print(np.mean(a1,axis=0))
# print(np.mean(a1,axis=1))

# print(np.median(a1))
# print(np.median(a1,axis=0))
# print(np.median(a1,axis=1))

# print(np.var(a1))


# a2 = np.arange(1,11).reshape(5,2)
# a3 = np.arange(11,21).reshape(2,5)

# a3 = np.dot(a2,a3)
# print(a2 @ a3)
# print(np.matmul(a2,a3))


# logs and exponents

# print(np.log(a1))
# print(np.exp(a1))

