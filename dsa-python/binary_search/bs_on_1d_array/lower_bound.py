# Given a sorted array of nums and an integer x, write a program to find the lower bound of x.

# The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

# If no such index is found, return the size of the array.

# Example 1
# Input : nums= [1,2,2,3], x = 2
# Output:1
# Explanation:
# Index 1 is the smallest index such that arr[1] >= x.


arr = [1, 3, 3, 3, 5]
# arr = [2,4,5,8,9,13,15,20,26,29,30]

x = 3

n = len(arr)

# ------------- Brute Force Approach -------------

# for i in range(n):
# 	if arr[i] >= x:
# 		print(i)
# 		break


# ------------- Optimal Approach -------------

# ----------- recursive way -------------

# def calLowerBound(arr,n,x,low,high):
# 	if low > high:
# 		return n
	
# 	mid = (low + high) // 2
# 	if arr[mid] >= x:
# 		high = mid - 1
# 		left_res = calLowerBound(arr,n,x,low,high)
# 		if left_res == n:
# 			return mid
# 		else:
# 			return left_res
# 	else:
# 		low = mid + 1
# 		return calLowerBound(arr,n,x,low,high)
		


# res = calLowerBound(arr,n,x,0,n-1)
# print(res)


# ----------- iterative way -------------

# low = 0
# high = n - 1
# res = n
# while low <= high:
# 	mid = (low + high) // 2

# 	if arr[mid] >= x:
# 		res = mid
# 		high = mid - 1
# 	else:
# 		low = mid + 1  

# print(res)