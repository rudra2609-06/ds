# LeetCode Notes:
# Problem: Find the length of the longest consecutive sequence in an unsorted array.
# Idea: Put values in a set and only start counting from sequence starts.
# Trick: If x-1 exists, then x is not a start, so skip it.
# Dry run: [102,4,100,1,101,3,2,1,1] -> start at 1 and count 1,2,3,4 -> answer 4.
# TC and SC: O(N) average time because set lookups are O(1), O(N) space because values are stored in a set.

l1 = [102,4,100,1,101,3,2,1,1]
res = 1


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time

# ------ Brute force approach ------
# for i in range(len(l1)):
# 	longest = 1
# 	element = l1[i]
# 	found = True

# 	while found:
# 		found = False
# 		for j in range(len(l1)):
# 			if l1[j] == element + 1:
# 				element += 1
# 				longest += 1
# 				found = True
			
			

# 	res = max(res,longest)

# print(res)

# --------- Better approach --------------

# l1 = [100,102,100,101,101,4,3,2,3,2,1,1,1,2]

# # sorts the l1 itself
# sorted_l1 = l1.sort()
# print(l1)

# # returns the sorted list and can be stored in variable
# # sorted_l1 = sorted(l1)
# # print(sorted_l1)

# last_small = 0
# count = 0
# res = 1

# for i in range(len(l1)):
# 	current_element = l1[i]
# 	diff = current_element - last_small
# 	if diff == 1:
# 		count += 1
# 		last_small = current_element
# 	elif diff > 1:
# 		count = 1
# 		last_small = current_element
# 	res = max(count,res)
	

# print(res)


# -------- optimal solution ------------ (only optimal under some constraint)

# l1 = [102,4,100,1,101,3,2,1,1]

# store them in set(unordered)

# s1 = set(l1)
# longest = 1

# print(s1)

# for element in s1:
# 	if element - 1 not in s1:
# 		count = 1
# 		starting_element = element
# 		while (starting_element + 1) in s1:
# 			starting_element  += 1
# 			count += 1

# 		longest = max(longest,count)

# print(longest)


# SC : O(N)
# TC : O(N)





