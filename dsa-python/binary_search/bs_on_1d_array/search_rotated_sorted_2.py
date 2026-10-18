# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

nums = [2,5,6,0,0,1,2]
target = 0

n = len(nums)
res = False

low = 0
high = n - 1

while low <= high:

	mid = (low + high) // 2

	if nums[mid] == target:
		res = True
		break
	# due to duplicate values existence we need to add this check
	elif nums[low] == nums[mid] == nums[high]:
		low += 1
		high -= 1
	elif nums[mid] >= nums[low]:
		if nums[low] <= target < nums[high]:
			high = mid - 1
		else:
			low = mid + 1
	else:
		if nums[mid] < target <= nums[high]:
			low = mid + 1
		else:
			high = mid - 1

print(res)
			
		