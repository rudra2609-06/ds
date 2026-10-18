# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.


fruits = [0,1,2,2]
n = len(fruits)
res = 0

# ------------ Brute Force Approach ------------ 

# for i in range(n):
# 	freq = {}
# 	for j in range(i,n):

# 		# add if absent else update
# 		if fruits[j] not in freq:
# 			freq[fruits[j]] = 1
# 		else:
# 			freq[fruits[j]] += 1

# 		if len(freq) > 2:
# 			res = max(res,j - i + 1)
# 			break
# 		res = max(res,j - i + 1)

# print(res)

# ------------ Optimal Approach ------------ 

# left = 0
# freq = {}

# for right in range(n):

# 	# if you do not have type add it else update
# 	if fruits[right] not in freq:
# 		freq[fruits[right]] = 1
# 	else:
# 		freq[fruits[right]] += 1

# 	# if freq > 2 then reduce left pointing type count to zero and then add new one on removing
# 	while len(freq) > 2:
# 		if fruits[left] in freq:
# 			freq[fruits[left]] -= 1

# 		if freq[fruits[left]] == 0:
# 			freq.pop(fruits[left],None)
# 		left += 1
# 	res = max(res,right - left + 1)

# print(res)


	





