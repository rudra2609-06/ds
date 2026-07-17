arr = [1, 2, 2, 3, 5, 6]
n = 6

# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.

# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.

# Example 1

# Input: nums = [3, 5, 4, 1, 1]

# Output: [1, 2]
# Explanation:
# 1 appears two times in the array and 2 is missing from nums

# ------------------ Brute Force Solution --------------

# for element in range(1,n + 1):
# 	found = 0
# 	for i in range(len(arr)):
# 		if arr[i] == element:
# 			found += 1
# 	if found == 0:
# 		res.insert(1,element)
# 	elif found > 1:
# 		res.insert(0,element)


# print(res)

# TC : O(N2)
# SC : O(1)

# ------------------ Optimal Solution --------------

# repeating = -1
# missing = -1

# for i in range(len(arr)):
# 	val = abs(arr[i])

# 	# check if value at index val -1 is negative
# 	if arr[val - 1] > 0:
# 		arr[val - 1] = -arr[val - 1]
# 	# if already negative
# 	else:
# 		repeating = val

# for i in range(len(arr)):
# 	if arr[i] > 0:
# 		missing = i + 1
# 		break

# print(repeating)
# print(missing)

# TC : O(N)
# SC : O(1)




