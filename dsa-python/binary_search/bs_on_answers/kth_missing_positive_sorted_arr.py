arr = [2,3,4,7,11]
k = 5
res = -1

# ---------- Brute Force ---------


# missing = []
# max_val = max(arr)

# for i in range(1,max_val):
# 	if i not in arr:
# 		missing.append(i)

# if len(missing) == 0:
# 	res = max_val + k
# else:
# 	res = missing[k - 1]


# print(res)


# ---------- Better Soln ---------

# num = 1
# missing = 0
# while True:
# 	if num not in arr:
# 		missing += 1
# 	if missing == k:
# 		res = num
# 		break
# 	num += 1
# print(res)

# ---------- Optimal Soln ---------

low = 0
high = len(arr) - 1

while low <= high:
	mid = (low + high) // 2

	missing = arr[mid] - (mid + 1)

	if missing > k:
		high = mid - 1
	else:
		low = mid + 1

res = low + k
print(res)






