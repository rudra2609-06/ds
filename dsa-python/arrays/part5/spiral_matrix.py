# you are given a n*m matrix
# you need to print it into spiral matrix

matrix = [
	[1,2,3,4,5,6],
	[20,21,22,23,24,7],
	[19,32,33,34,25,8],
	[18,31,36,35,26,9],
	[17,30,29,28,27,10],
	[16,15,14,13,12,11]
]

cols = len(matrix[0])
rows = len(matrix)

# ---------- This problem has only 1 soln that is optimal soln ------------

left = 0
right = cols - 1
bottom = rows - 1
top = 0

spiral_matrix = []

while top <= bottom and left <= right:
	# move from left to right and print top row

	for i in range(left,right + 1):
		spiral_matrix.append(matrix[top][i])

	top += 1

	# move from top to btm and print right row
	for j in range(top,bottom + 1):
		spiral_matrix.append(matrix[j][right])


	right -= 1	

	# move from right to left and print bottommost row
	if top <= bottom:
		for k in range(right,left - 1,-1):
			spiral_matrix.append(matrix[bottom][k])
		bottom -= 1



	# move from bottom to top and print left most row
	if left <= right:
		for l in range(bottom,top - 1,-1):
			spiral_matrix.append(matrix[l][left])
		left += 1


print(spiral_matrix)



