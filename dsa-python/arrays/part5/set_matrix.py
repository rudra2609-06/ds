# LeetCode Notes:
# Problem: If a cell is 0, make its full row and column 0 using only original zero positions.
# Idea: Use first row and first column as marker storage.
# Trick: Save whether the first row or first column had a zero before using them as markers.
# Dry run: zero positions mark their row and column, then marked rows and cols are turned to 0.
# TC and SC: O(N*M) time because the matrix is scanned a few times, O(1) space because markers are inside the matrix.

# we are given n*m matrix constisting only 1 and 0 what i need to do is wherever i find 0 that row and that col should be converted to 0 after that
# there is catch in problem only those 0 should be converted which are present initially in the problem not those which are converted 


matrix = [
	[1,1,1,1],
	[1,0,0,1],
	[1,1,0,1],
	[1,1,1,1]
]

cols = 4
rows = 4

# --------- Brute Force Approach ------------

# def markRow(row_idx):
# 	for col in range(cols):
# 		if matrix[row_idx][col] != 0:
# 			matrix[row_idx][col] = -1

# def markCol(col_idx):
# 	for row in range(rows):
# 		if matrix[row][col_idx] != 0:
# 			matrix[row][col_idx] = -1

# for row_i in range(rows):
# 	for col_j in range(cols):
# 		if matrix[row_i][col_j] == 0:
# 			markRow(row_i)
# 			markCol(col_j)


# for i in range(rows):
# 	for j in range(cols):
# 		if matrix[i][j] == -1:
# 			matrix[i][j] = 0

# print(matrix)

# -------------- Better Approach --------------

# zero_rows = set()
# zero_cols = set()

# for i in range(rows):
# 	for j in range(cols):
# 		if matrix[i][j] == 0:
# 			zero_rows.add(i)
# 			zero_cols.add(j)


# 
# 
# 
# 
#  print(zeros_idx)

# for i in range(rows):
# 	for j in range(cols):
# 		if i in zero_rows or j in zero_cols:
# 			matrix[i][j] = 0


# print(matrix)

# TC : O(N*M)
# SC: O(N*M)

# --------- Optimal Approach ---------

first_row_zero = False
first_col_zero = False


# check if first row contains 0
for col_idx in range(cols):
	if matrix[0][col_idx] == 0:
		first_row_zero = True
		break


# check if first col contains 0

for row_idx in range(rows):
	if matrix[row_idx][0] == 0:
		first_col_zero = True
		break



# using first row and first col as markers

for row_idx in range(1,rows):
	for col_idx in range(1,cols):
		if matrix[row_idx][col_idx] == 0:
			matrix[row_idx][0] = 0
			matrix[0][col_idx] = 0
	
# now utilizing markers into inner cells
for row_idx in range(1,rows):
	for col_idx in range(1,cols):
		if matrix[row_idx][0] == 0 or matrix[0][col_idx] == 0:
			matrix[row_idx][col_idx] = 0

# if first row is 0
if first_row_zero:
	for col_idx in range(cols):
		matrix[0][col_idx] = 0

# if first col is 0
if first_col_zero:
	for row_idx in range(rows):
		matrix[row_idx][0] = 0

print(matrix)
print(first_row_zero)
print(first_col_zero)










