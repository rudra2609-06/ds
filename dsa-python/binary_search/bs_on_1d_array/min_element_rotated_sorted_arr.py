# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

nums = [3,4,5,1,2]
n = len(nums)
low = 0
high = n - 1


while low < high:
	mid = (low + high) // 2

	if nums[mid] > nums[high]:
		low = mid + 1
	else:
		high = mid

print(nums[high])


