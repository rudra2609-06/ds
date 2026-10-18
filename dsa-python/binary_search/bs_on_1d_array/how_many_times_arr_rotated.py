# Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.

# Example 1
# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]
# Output: 4
# Explanation: The original array should be [0, 1, 2, 3, 4, 5, 6, 7]. So, we can notice that the array has been rotated 4 times.

# idea simply -> idx of minimum element will say how many times arr is rotated

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

print(high)

# if arr would have left rotated
# Right rotations = index of minimum element
# Left rotations = (len(arr) - index_of_minimum) % len(arr)

# for arr to be rotated k time right side. right rotation brings last element front each time

# -------------------- right rotation --------------------

# [1, 2, 3, 4, 5] i need to rotate right side by 3 time

# Right rotation 1 time
# [5, 1, 2, 3, 4]

# Right rotation 2 times
# [4, 5, 1, 2, 3]

# Right rotation 3 times
# [3, 4, 5, 1, 2]

# in another way last k elements put them in front of remaining elements


# -------------------- left rotation --------------------

# For left rotation, you move the first element to the end each time.

# Left rotation 1 time
# [2, 3, 4, 5, 1]

# Left rotation 2 times
# [3, 4, 5, 1, 2]

# Left rotation 3 times
# [4, 5, 1, 2, 3]

# in another way take first k elements put them in after of remaining elements