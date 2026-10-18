# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].


nums = [1,1,2,1,1]
k = 3

# ------------------ Brute Force Approach ------------------

# n = len(nums)
# res = 0

# for i in range(n):
# 	no_of_odds = 0
# 	for j in range(i,n):
# 		if nums[j] % 2 != 0:
# 			no_of_odds += 1
# 		if no_of_odds == k:
# 			res += 1

# print(res)

# ------------------ Optimal Approach ------------------

# class Solution:
# 	def numberOfSubarrays(self,nums: List[int],k : int) -> int:
# 		return self.atMost(nums,k) - self.atMost(nums,k - 1)

# 	def atMost(self,nums,k : int) -> int:
# 		n = len(nums)
# 		res = 0
# 		total_odd_counts = 0
# 		left = 0

# 		for right in range(n):
# 			if nums[right] % 2 != 0:
# 				total_odd_counts += 1
			
# 			while total_odd_counts > k:
# 				if nums[left] % 2 != 0:
# 					total_odd_counts -= 1
# 				left += 1
			
# 			res += right - left + 1
# 		return res

# s1 = Solution()
# res = s1.numberOfSubarrays(nums,k)
# print(res)