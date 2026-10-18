# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

arr = [1,3,4,5,6]
x = 3

n = len(arr)

low = 0
high = n - 1

res = n

while low <= high:
	mid = (low + high) // 2

	if arr[mid] == x:
		res = mid
		break
	elif arr[mid] > x:
		res = mid
		high = mid - 1
	else:
		low = mid + 1

print(res)