# LeetCode Notes:
# Problem: Pascal Triangle questions can ask for one value, one row, or the full triangle.
# Idea: Build each next value from the previous value instead of using full factorial every time.
# Trick: next = prev * (row - col) // col gives the next element in the same row.
# Dry run: row 5 becomes 1,4,6,4,1.
# TC and SC: O(N^2) time to print N rows because all values are generated, O(1) extra space if output is ignored.

# there could three types of questions that can be asked in this pascal triangle problem

# 1] Given Row number and col number tell me the element
# 2] Given Row number print that particular row
# 3] Print whole pascal's triangle


# row number = 5 and col number = 3

# r - 1 C c - 1
# nCr = !n / !r * (n - r)!

row_number = 5
col_number = 3

# n1 = 1
# d1 = 1

# value = 0

# i = 0
# limit = col_number - 1

# while i < limit:
# 	n1 *= row_number - 1
# 	d1 *= col_number - 1
# 	print(i)
# 	print(n1,d1)

# 	row_number -= 1
# 	col_number -= 1
# 	i += 1

# value = n1//d1
# print(value)

# TC : O(col)
# SC : O(1)

# ------------ Print Any given row ----------------

# row_number = 6 #(1 based)

# prev_element = 1
# nums = []
# nums.append(1)
# row = row_number

# for i in range(1,6):
# 	next_element = prev_element * (row - i) // (i)
# 	nums.append(next_element)    
# 	prev_element = next_element


# print(nums)

# TC : O(row)
# SC : O(1)


# ----------- Given N print whole pascal triangle ---------------

n = 6 # (1 based)

nums = []

for i in range(1,n + 1):	
	# print members of that rows
	prev_element = 1
	nums.append(1)
	for j in range(1,i):
		next_element = prev_element * (i - j) // j
		nums.append(next_element)
		prev_element = next_element
	

print(nums)











