# Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice. Find the single number in the array.

# Example 1
# Input :nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
# Output:4
# Explanation: Only the number 4 appears once in the array.



nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

n = len(nums)

low = 0
high = n - 1

while low < high:
	mid = (low + high) // 2

	# it is even
	if mid % 2 == 0:
		# first el
		if nums[mid] == nums[mid + 1]:
			low = mid + 1
		else:
			high = mid
	# it is odd
	else:
		# first el
		if nums[mid] == nums[mid + 1]:
			high = mid
		else:
			low = mid + 1
		



print(nums[high])