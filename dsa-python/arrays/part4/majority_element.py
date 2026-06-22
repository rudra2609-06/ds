# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


l1 = [2,2,3,3,1,2,2]

size_by_2 = len(l1) // 2 

# -------------- brute force approach --------------

# majority_occuring_element = -1

# for i in range(len(l1)):
# 	count = 0
# 	for j in range(len(l1)):
# 		if l1[i] == l1[j]:
# 			count += 1
		
# 	if count > size_by_2:
# 		majority_occuring_element = l1[i]
# 		break

# print(majority_occuring_element)



# -------------- better approach --------------

# hash_l1 = [0] * (max(l1) + 1)

# for i in range(len(l1)):
# 	hash_l1[l1[i]] += 1

# majority_occuring_element = -1

# for i in range(len(hash_l1)):
# 	if hash_l1[i] > size_by_2:
# 		majority_occuring_element = i
# 		break

# print(size_by_2)
# print(majority_occuring_element)
    
# -------------- optimal approach --------------

# Boyer's Moore Majority Voting Algorithm

# candidate = -1
# votes = 0

# for i in range(len(l1)):
# 	if votes == 0:
# 		candidate = l1[i]
# 		votes = 1
# 	else:
# 		if l1[i] == candidate:
# 			votes += 1
# 		else:
# 			votes -= 1


# count = 0
# for i in range(len(l1)):
# 	if l1[i] == candidate:
# 		count += 1

# if count > size_by_2:
# 	print(candidate)
# else:
# 	print(-1)
	

# Time Complexity : O(N)
#Space Complexity : O(1)

