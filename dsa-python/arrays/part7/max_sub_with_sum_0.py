# You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.

# Return the length of such a subarray. If no such subarray exists, return 0.

# Example 1

# Input: arr = [15, -2, 2, -8, 1, 7, 10, 23]

# Output: 5

# Explanation:

# The subarray [-2, 2, -8, 1, 7] sums up to 0 and has the maximum length among all such subarrays.


arr = [1, 0, -4, 3, 1, 0]
res = 0
n = len(arr)

# ------------- Brute Force Approach -------------

# for i in range(n):
# 	total = 0
# 	for j in range(i,n):
# 		total += arr[j]
# 		if total == 0:
# 			length = j - i + 1
# 			res = max(res,length)

# print(res)

# ------------- Optimal Approach -------------

last_sum = 0
res = 0

prefixSum = 0
prefixSumMap = {0:-1}
res = 0

for i in range(n):
	prefixSum += arr[i]

	if prefixSumMap.get(prefixSum) != None:
		length = i - prefixSumMap[prefixSum]
		res = max(res,length)
	
	if prefixSum not in prefixSumMap:
		prefixSumMap[prefixSum] = i

print(res)


	


