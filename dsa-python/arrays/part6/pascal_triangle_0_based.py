# LeetCode Notes:
# Problem: Print a Pascal Triangle row when row number is 0-based.
# Idea: Start from 1 and keep building the next value from the previous one.
# Trick: One row can be generated left to right without storing old rows.
# Dry run: row=4 -> 1,4,6,4,1.
# TC and SC: O(row) time because row+1 values are generated once, O(1) extra space because only prev value is stored.

# we have given row_number = 4 (0-based) we need to calculate row elements and print it

# total elements in a row = row_number + 1 (0-based)

# first element = 1 (always)

# next_element = prev * factor

# factor = (row - col_idx + 1) // i


row = 4

prev_element = 1
total_elements = row + 1
print(prev_element)

# because from total elements 1 at idx 0 we already know so we need to start from 1 to total elements 
for col_idx in range(1,total_elements):
	next_element = prev_element * (row - col_idx + 1) // col_idx
	print(next_element)
	prev_element = next_element
