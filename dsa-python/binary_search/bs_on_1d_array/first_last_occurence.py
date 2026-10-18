arr = [5,7,7,8,8,10]
n = len(arr)
target = 8
first = -1
last = -1

# ------------------ Brute Force Approach ------------------

# for i in range(n):
# 	if arr[i] == target and first == -1:
# 		first = i
# 	elif arr[i] == target and first != -1:
# 		last = i
	
# print(first,last)

# ------------------ Optimal Approach ------------------

low = 0
high = n - 1

# left bs 
while low <= high:
	mid = (low + high) // 2
	
	if arr[mid] == target:
		first = mid
		high = mid - 1
	elif arr[mid] > target:
		high = mid - 1
	else:
		low = mid + 1

low = 0
high = n - 1

# right bs 
while low <= high:
	mid = (low + high) // 2
	if arr[mid] == target:
		last = mid
		low = mid + 1
	elif arr[mid] > target:
		high = mid - 1
	else:
		low = mid + 1

print(first,last)


