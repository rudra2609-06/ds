# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.



# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.



arr = [1,2,3,4,5,6,1]
k = 3

# window_sum = sum(arr[:k])
# right = len(arr) - 1

# res = window_sum


# for i in range(k):
# 	window_sum = window_sum - arr[k - i - 1] + arr[right]
# 	print(window_sum)
# 	res = max(res,window_sum)
# 	right -= 1


# # print(res)








	

