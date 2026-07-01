arr = [1, 2, 2, 3, 5, 6]
n = 6

# ------------------ Brute Force Solution --------------

# for element in range(1,n + 1):
# 	found = 0
# 	for i in range(len(arr)):
# 		if arr[i] == element:
# 			found += 1
# 	if found == 0:
# 		res.insert(1,element)
# 	elif found > 1:
# 		res.insert(0,element)


# print(res)

# TC : O(N2)
# SC : O(1)

# ------------------ Optimal Solution --------------

# repeating = -1
# missing = -1

# for i in range(len(arr)):
# 	val = abs(arr[i])

# 	# check if value at index val -1 is negative
# 	if arr[val - 1] > 0:
# 		arr[val - 1] = -arr[val - 1]
# 	# if already negative
# 	else:
# 		repeating = val

# for i in range(len(arr)):
# 	if arr[i] > 0:
# 		missing = i + 1
# 		break

# print(repeating)
# print(missing)

# TC : O(N)
# SC : O(1)




