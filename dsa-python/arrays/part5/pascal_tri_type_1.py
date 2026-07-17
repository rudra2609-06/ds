# given row no. and col no. find element at that position

# ---------------- row no. and col no. both are 0 based indexing ----------------

# row_no = 6
# col_no = 2
# n = row_no
# r = col_no
# k = min(n,r)

# r1 = 1
# c1 = 1
# i = 1
# while i <= k:
#     r1 *= row_no
#     c1 *= col_no
#     row_no -= 1
#     col_no -= 1
#     i += 1

# print(r1 // c1)


# ---------------- row no. and col no. both are 1 based indexing ----------------

# update row_no and col_no by subtracting 1 from each before cal

# row_no = 6
# col_no = 2

# row_no = 5
# col_no = 1
# n = row_no
# r = col_no
# k = min(n,r)

# r1 = 1
# c1 = 1
# i = 1
# while i <= k:
#     r1 *= row_no
#     c1 *= col_no
#     row_no -= 1
#     col_no -= 1
#     i += 1

# print(r1 // c1)
