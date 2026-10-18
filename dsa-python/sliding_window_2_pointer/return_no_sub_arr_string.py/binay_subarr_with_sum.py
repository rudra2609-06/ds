# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

arr = [1,0,1,0,1]
goal = 2



# ------------------ Brute Force Approach ------------------

# n = len(arr)
# res = 0

# for i in range(n):
# 	total = 0
# 	for j in range(i,n):
# 		total += arr[j]
# 		# if total != goal:
# 			# break
# 		if total == goal:
# 			res += 1



# print(res)

# ------------------ Optimal Approach ------------------

def numSubarraysWithSum(arr,goal):
	return atMost(arr,goal) - atMost(arr,goal - 1)

def atMost(arr,goal):
	n = len(arr)
	total = 0
	left = 0
	res = 0

	for right in range(n):
		total += arr[right]

		while total > goal:
			total -= arr[left]
			left += 1
		
		win_size = right - left + 1
		res += win_size
	return res

print(numSubarraysWithSum(arr,goal))

