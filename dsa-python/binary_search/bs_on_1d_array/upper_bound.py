# Given a sorted array of nums and an integer x, write a program to find the upper bound of x.

# The upper bound of x is defined as the smallest index i such that nums[i] > x.

# If no such index is found, return the size of the array.



arr = [1, 3, 3, 3, 5]
target = 3

n = len(arr)

# ------------- Brute Force Approach -------------

# for i in range(n):
# 	if arr[i] > target:
# 		print(i)
# 		break


# ------------- Optimal Approach -------------

# ----------- recursive way -------------

# def upperBound(arr,n,x,low,high):
# 	if low > high:
# 		return n
	
# 	mid = (low + high) // 2

# 	if arr[mid] > target:
# 		high = mid - 1
# 		res = upperBound(arr,n,x,low,high)
# 		if res == n:
# 			return mid
# 		else:
# 			return res
# 	else:
# 		low = mid + 1
# 		return upperBound(arr,n,x,low,high)

# res = upperBound(arr,n,target,0,n-1)
# print(res)


# ----------- iterative way -------------

# low = 0
# high = n - 1
# res = n
# while low <= high:
# 	mid = (low + high) // 2

# 	if arr[mid] > target:
# 		res = mid
# 		high = mid - 1
# 	else:
# 		low = mid + 1

# print(res)