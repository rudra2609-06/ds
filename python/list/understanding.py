# ==========================
# Python List Slicing Notes
# ==========================

# General Syntax:
# list[start:stop:step]

# Important Rules:
# 1. stop index is ALWAYS excluded.
# 2. Default step = +1.
# 3. Positive step (+1):
#    start should be less than stop.
#    Otherwise the slice is empty.
#
# 4. Negative step (-1):
#    start should be greater than stop.
#    Otherwise the slice is empty.

# ----------------------------------
# Converting Negative Indices
# ----------------------------------

# Formula:
# positive_index = len(list) + negative_index

# Example:
# L = [1,2,3,4]
#
# Negative -> Positive
# -4 -> 0
# -3 -> 1
# -2 -> 2
# -1 -> 3

# ----------------------------------
# Understanding Slices
# ----------------------------------

# L[-2:-1]
# becomes L[2:3]
# Result: [3]

# L[-1:-2]
# becomes L[3:2]
# step = +1
# Result: []

# L[-1:-2:-1]
# becomes L[3:2:-1]
# Result: [4]

# ----------------------------------
# Mental Model
# ----------------------------------

# Step 1:
# Convert negative indices to positive.

# Step 2:
# Identify start, stop, and step.

# Step 3:
# Ask:
# "Can I reach stop from start using this step?"

# Examples:
#
# L[2:0]
# step = +1
# Cannot move from 2 to 0 using +1
# Result: []
#
# L[2:0:-1]
# Can move 2 -> 1
# Result: [element at index 2, element at index 1]

# ----------------------------------
# del with Slices
# ----------------------------------

# del removes all elements selected by the slice.

# Example:
# L = [10,20,30,40,50,60]
#
# del L[-2:-6:-2]
#
# Convert:
# del L[4:0:-2]
#
# Selected indices:
# 4 -> 2
#
# Selected values:
# [50,30]
#
# Result:
# [10,20,40,60]

# ----------------------------------
# Quick Revision Rule
# ----------------------------------

# Positive step (+):
# move LEFT -> RIGHT
# start < stop

# Negative step (-):
# move RIGHT -> LEFT
# start > stop

# If direction and step don't match,
# the slice is EMPTY.