# LeetCode Notes:
# Problem: Find all elements that appear more than n/3 times.
# Idea: There can be at most two such elements, so keep two candidates and two counts.
# Trick: Use extended Boyer-Moore voting, then verify both candidates once at the end.
# Dry run: [1,1,1,3,3,2,2,2] -> candidates become 1 and 2, both pass the final count check.
# TC and SC: O(N) time because we do linear scans, O(1) space because only a few variables are used.

l1 = [1,1,1,3,3,2,2,2]

size_by_3 = len(l1) // 3
# count = 0
# majority_elements = []

# ---------------- Brute Force Approach ----------------------


# for i in range(len(l1)):
# 	if l1[i] not in majority_elements:
# 		element = l1[i]
# 		count = 0
# 	for j in range(len(l1)):
# 		if element == l1[j]:
# 			count += 1
# 		if count > size_by_3 and element not in majority_elements:
# 			majority_elements.append(element)
# 			break

# print(majority_elements)


# TC : O(N2)
# SC: O(1) for solving the problem and for storing the problem at max O(len(l1) // 4)
	

# -------------- Better Approach ---------------

# hash_l1 = [0] * (max(l1) + 1)
# majority_elements = []

# for i in range(len(l1)):
# 	hash_l1[l1[i]] += 1

# for j in range(len(hash_l1)):
# 	if hash_l1[j] > size_by_3:
# 		majority_elements.append(j)

# print(majority_elements)

# TC : O(N + max(N))
# SC : O(max(N))


# ---------------- Optimal Approach ----------------



# majority_elements = []

# c1,c2 = -1,-1
# v1,v2 = 0,0

# for i in range(len(l1)):
# 	if l1[i] == c1:
# 		v1 += 1
# 	elif l1[i] == c2:
# 		v2 += 1
# 	elif v1 == 0:
# 		c1 = l1[i]
# 		v1 = 1
# 	elif v2 == 0:
# 		c2 = l1[i]
# 		v2 = 1
# 	else:
# 		v1 -= 1
# 		v2 -= 1

# # check if both are majority or not

# print(c1)
# print(c2)
# count1 = 0
# count2 = 0

# for element in l1:
# 	if element == c1:
# 		count1 += 1
# 	elif element == c2:
# 		count2 += 1

# if count1 > size_by_3:
# 	majority_elements.append(c1)

# if count2 > size_by_3:
# 	majority_elements.append(c2)

# print(majority_elements)

# TC: O(N)
# SC: O(1)


	
	

