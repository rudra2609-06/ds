import numpy as np

# if we do not have built in fn and we still want to a apply mathematical fn to it we can make it in numpy

# sigmoid

# def sigmoid(arr):
# 	return 1 / (1 + ((np.exp(-(arr)))))

# a = np.arange(10)

# res = sigmoid(a)
# print(res)

# mean squared error

# def mse(a,p):
# 	return np.mean((a - p) ** 2)


# actual = np.random.randint(1,50,25)
# predicted = np.random.randint(1,50,25)

# res = mse(actual,predicted)
# print(res)

# binary cross entropy



# ---------- working with missing values -> np.nan(array) ------------

# null and nan is not same nan is only missing values

# a = np.array([1,2,3,4,np.nan,5,6])
# print(a)

# clearing missing values: boolean indexing

# i do not want any nan values 
# print(a[(~np.isnan(a))])

# ------------- Plotting Graphs -------------
import matplotlib.pyplot as plt

# plotting a 2D graph

# x = y (straight line)

# x = np.linspace(-10,10,100)
# y = x


# plt.plot(x,y)
# plt.show()

# y = x2 (Parabola)
# x = np.linspace(-10,10,100)
# y = x ** 2


#plt.plot(x,y)
# plt.show()

# y = sin(x)

# x = np.linspace(-10,10,100)
# y = np.sin(x)

# plt.plot(x,y)
# plt.show()

# y = x log(x)
# x = np.linspace(-10,10,100)
# y = x * (np.log(x))

# plt.plot(x,y)
# plt.show()









