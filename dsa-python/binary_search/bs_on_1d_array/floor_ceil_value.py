# Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.


# Example 1
# Input : nums =[3, 4, 4, 7, 8, 10], x= 5
# Output: 4 7
# Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

nums = [3, 4, 4, 7, 8, 10]
x = 8
n = len(nums)

# ------------- Brute Force Approach -------------

# floor_val = -1
# ceil_val = -1

# for num in nums:
# 	if num < x :
# 		floor_val = max(floor_val,num)
# 	elif num > x:
# 		if ceil_val == -1:
# 			ceil_val = num
# 		else:
# 			ceil_val = min(num,ceil_val)
# 	else:
# 		floor_val = num
# 		ceil_val = num
# 		break

# print(floor_val)
# print(ceil_val)


# ------------- Optimal Approach -------------


def floorCeilVal(arr,low,high):
	floorVal = -1
	ceilVal = -1

	while low <= high:
		mid = (low + high) // 2

		if arr[mid] == x:
			floorVal = arr[mid]
			ceilVal = arr[mid]
			break
		elif arr[mid] < x:
			low = mid + 1
			floorVal = arr[mid]
		else:
			high = mid - 1
			ceilVal = arr[mid]
	return list([floorVal,ceilVal])

res = floorCeilVal(nums,0,len(nums))
print(res)

