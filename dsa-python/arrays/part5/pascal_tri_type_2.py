# given row no. print elements of that row

# ---------------- row no. 0 based indexing ----------------

row_no = 4

prev_factor = 1

total_element = row_no + 1

print(prev_factor)
for i in range(1,total_element):
    factor = (row_no - i + 1) / i
    element = prev_factor * factor
    print(element)
    prev_factor = element
    

# ---------------- row no. 1 based indexing ----------------

# update row_no subtracting 1 before cal


row_no = 5

prev_factor = 1


row_no = row_no - 1
total_element = row_no + 1

print(prev_factor)
for i in range(1,total_element):
    factor = (row_no - i + 1) / i
    element = prev_factor * factor
    print(element)
    prev_factor = element
    
