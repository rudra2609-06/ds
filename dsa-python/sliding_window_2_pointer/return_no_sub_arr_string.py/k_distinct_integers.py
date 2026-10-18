# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.


nums = [1,2,1,2,3]
k = 2

# ---------------- Brute Force Approach ----------------

# n = len(nums)
# res = 0

# for i in range(n):
# 	freq = {}
# 	for j in range(i,n):
# 		if nums[j] in freq:
# 			freq[nums[j]] += 1
# 		else:
# 			freq[nums[j]] = 1
		
# 		if len(freq) == k:
# 			res += 1
# 		elif len(freq) > k:
# 			break
# print(res)


# ---------------- Optimal Approach ----------------

def k_distinct_integers(nums,k):
	return atMost(nums,k) - atMost(nums,k-1)

def atMost(nums,k):
	res = 0
	n = len(nums)
	left = 0
	freq = {}
	for right in range(n):
		if nums[right] in freq:
			freq[nums[right]] += 1
		else:
			freq[nums[right]] = 1

		while len(freq) > k:
			freq[nums[left]] -= 1
			if freq[nums[left]] == 0:
				freq.pop(nums[left],None)
			left += 1
		res += right - left + 1
	return res


res = k_distinct_integers(nums,k)
print(res)