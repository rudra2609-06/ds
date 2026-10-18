arr1 = [1,3,4,7,10,12]
arr2 = [2,3,6,15]


n1 = len(arr1)
n2 = len(arr2)

# ----------------- Brute Force -----------------
# TC : O(n1 + n2)
# SC : O(n1 + n2)

# arr3 = []

# i = 0
# j = 0
# res = -1

# while i < n1 and j < n2:
# 	if arr1[i] <= arr2[j]:
# 		arr3.append(arr1[i])
# 		i += 1
# 	else:
# 		arr3.append(arr2[j])
# 		j += 1

# while i < n1:
# 	arr3.append(arr1[i])
# 	i += 1

# while j < n2:
# 	arr3.append(arr2[j])
# 	j += 1

# if (n1 + n2) % 2 == 0:
# 	res = (arr3[n1 // 2]) + (arr3[ (n2 // 2) - 1 ])
# else:
# 	res = arr3[n1 // 2]

# print(res)


# ----------------- Better Approach -----------------

# TC : O(n1 + n2)
# SC : O(1)

i = 0
j = 0

cnt = 0
idx1 = (n1 + n2) // 2
idx2 = idx1 - 1
elem1 = elem2 = -1

res = -1

while i < n1 and j < n2:
	if elem1 != -1 and elem2 != -1:
		break
	elif arr1[i] < arr2[j]:
		if cnt == idx1:
			elem1 = arr1[i]
		if cnt == idx2:
			elem2 = arr1[i]
		cnt += 1
		i += 1
	else:
		if cnt == idx1:
			elem1 = arr2[j]
		if cnt == idx2:
			elem2 = arr2[j]
		cnt += 1
		j += 1

if elem1 == -1 or elem2 == -1:
	while i < n1:
		if cnt == idx1:
			elem1 = arr1[i]
		if cnt == idx2:
			elem2 = arr1[i]
		cnt += 1
		i += 1

if elem1 == -1 or elem2 == -1:
	while j < n2:
		if cnt == idx1:
			elem1 = arr2[j]
		if cnt == idx2:
			elem2 = arr2[j]
		cnt += 1
		j += 1

if (n1 + n2) % 2 == 0:
	res = (elem1 + elem2) / 2
else:
	res = elem1

print(res) 