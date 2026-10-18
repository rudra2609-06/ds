arr = [0, 0, 1, 1, 1, 2, 3]
target = 1
n = len(arr)

# ------------------ Brute Force Approach ------------------

count = 0
for i in range(n):
	if arr[i] == target:
		count += 1

print(count)


# ------------------ Optimal Approach ------------------

first = -1
last = - 1

low = 0
high = n - 1

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

while low <= high:
	mid = (low + high) // 2

	if arr[mid] == target:
		last = mid
		low = mid + 1
	elif arr[mid] > target:
		high = mid - 1
	else:
		low = mid + 1

if last != -1 and first != -1:
	res = last - first + 1
else:
	res = 0