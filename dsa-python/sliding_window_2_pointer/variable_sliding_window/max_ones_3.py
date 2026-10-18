# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
n = len(nums)
res = 0

# ------------- Brute Force Approach -------------

# idx1 = -1
# idx2 = -1
# for i in range(n):
# 	zeroes = 0
# 	for j in range(i,n):
# 		if nums[j] == 0:
# 			zeroes += 1
# 		if zeroes <= k:
# 			if res < (j - i + 1):
# 				res = j - i + 1
# 				idx1 = i
# 				idx2 = j


# print(res)
# print(nums[idx1 : idx2 + 1])


# ------------- Optimal Approach -------------

# left = 0
# zeroes = 0

# for right in range(n):
# 	if nums[right] == 0:
# 		zeroes += 1
	
# 	while zeroes > k:
# 		if nums[left] == 0:
# 			zeroes -= 1
# 		left += 1
	
# 	res = max(res,right - left + 1)

# print(res)