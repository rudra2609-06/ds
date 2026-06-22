# we have n*n square matrix we need to rotate it by 90 deg clockwise

# if matrix is square matrix than no.of rows = no.of cols

matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]

rows = len(matrix)
cols = len(matrix)

# how to generate this
# rotated_matrix = [
# 	[0,0,0,0],
# 	[0,0,0,0],
# 	[0,0,0,0],
# 	[0,0,0,0]
# ]
# rotated_matrix = []

# # for row_idx in range(rows):
# # 	new_row = [0] * cols
# # 	rotated_matrix.append(new_row)

# # print(rotated_matrix)

# for row_idx in range(rows):
# 	for col_idx in range(cols):
# 		rotated_matrix[row_idx][col_idx] = matrix[cols - col_idx - 1][row_idx]

# print(rotated_matrix)

# Time = O(N²)
# Space = O(N²)

# for row_idx in range(rows):
# 	for col_idx in range(row_idx + 1,cols):
# 		matrix[row_idx][col_idx],matrix[col_idx][row_idx] = matrix[col_idx][row_idx],matrix[row_idx][col_idx]
		
		
# for row in matrix:
# 	row.reverse()

# print(matrix)

# TC = O(N2)
# SC = O(1)
		



