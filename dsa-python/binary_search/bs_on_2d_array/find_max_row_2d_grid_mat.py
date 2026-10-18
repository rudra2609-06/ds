mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]

rows = len(mat)
cols = len(mat[0])

# --------------- Brute Force Approach ---------------

# res = -1
# resCount = 0
# for i in range(rows):
# 	count = 0
# 	for j in range(cols):
# 		if mat[i][j] == 1:
# 			count += 1
# 	if count > resCount:
# 		res = i
# 		resCount = count


# print(res)
# TC : n (no.of.rows) * =n(no.of.cols)
# SC : O(1)


# --------------- Better Approach ---------------

# def maxOnes(row,cols,target):
# 	low = 0
# 	high = cols - 1

# 	while low <= high:
# 		mid = (low + high) // 2

# 		if row[mid] >= target:
# 			high = mid - 1
# 		else:
# 			low = mid + 1

# 	return low if low < len(row) else -1
	

# res = -1
# resCnt = 0
# for i in range(rows):

# 	idx = maxOnes(mat[i],cols,1)

# 	if (idx != -1) and (cols - idx > resCnt):
# 		res = i
# 		resCnt = cols - idx

# print(res)


# TC : n (no.of.rows) * log(no.of.cols)
# SC : O(1)

# --------------- Optimal Approach ---------------

# r = 0
# c = cols - 1
# res = -1
# while r < rows and c >= 0:
# 	if mat[r][c] == 0:
# 		r += 1
# 	else:
# 		res = r
# 		c -= 1

# print(res)

# TC : n (no.of.rows) + (no.of.cols)
# SC : O(1)





		