# LeetCode Notes:
# Problem: Find the next lexicographically greater permutation.
# Idea: Find the first drop from the right, swap it with the next bigger value, then reverse the suffix.
# Trick: The suffix is already decreasing, so reversing it gives the smallest valid next order.
# Dry run: [2,1,5,4,3,0,0] -> pivot 1, swap with 3, reverse right side -> [2,3,0,0,1,4,5].
# TC and SC: O(N) time because we scan and reverse once, O(1) space because it is in-place.

l1 = [2,1,5,4,3,0,0]          

# brute force approach

# 1. Generate all permutations in sorted manner
# 2. To linear search the index of current list
# 3. Return the very next idx or if not there then first index

# time complexity: O(N * !N)


# ------------ Optimal Solution -------------

# idx = -1
# next_permutation = []

# for i in range(len(l1) - 2,-1,-1):
# 	if l1[i] < l1[i + 1]:
# 		idx = i
# 		break

# # print(idx)

# if idx == -1:
# 	next_permutation = l1[::-1]

# for i in range(len(l1) - 1,idx,-1):
# 	if l1[i] > l1[idx]:
# 		l1[i],l1[idx] = l1[idx],l1[i]
# 		break

# print(l1)

# reversed_part = l1[len(l1) -1:idx: -1]
# print(reversed_part)

# next_permutation = l1[:idx + 1] + reversed_part

# ------ OR ------

# next_permutation = l1[:idx + 1] + l1[idx + 1:][::-1]



# print(next_permutation)













