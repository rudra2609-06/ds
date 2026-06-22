# You are given an array which has equal number of positives and negatives in it therefore array size will be always even. You need to re-arrange that array.
#Rearrange means one positive,one negative,one positive,...

# l1 = [3,1,-2,-5,2,-4]

# output : [3,-2,1,-5,2,-4]

# -------------- brute force approach --------------

# all_positives = []
# all_negatives = []

# for element in l1:
# 	if element >= 0:
# 		all_positives.append(element)
# 	else:
# 		all_negatives.append(element)


# for i in range(len(l1)//2):
# 	l1[i * 2] = all_positives[i]
# 	l1[(i * 2) + 1] = all_negatives[i]


# print(l1)	

# Space complexity: O(2N)
# Time complexity: O(2N)

# if interviewer ask can we remove extra space we can't here becasue we need to store them somewhere
#but we can optimize number of passess taken

# -------------- optimal approach --------------


# pos_idx = 0
# negative_idx = 1

# res = [0] * len(l1)

# for i in range(len(l1)):
# 	if l1[i] >= 0:
# 		res[pos_idx] = l1[i]
# 		pos_idx += 2
# 	else:
# 		res[negative_idx] = l1[i]
# 		negative_idx += 2

# print(res)


# Space complexity: O(N)
# Time complexity: O(N)


# --------------------- Another Variety ---------------------

# given that the array will contain positive and negative numbers but not equal they will unequal
#still we have to re-arrange them alternatively but if any number left just add them so preserve the relative order
# fall back to brute force

# l1 = [1,2,-4,-5,3,-1,6,7]


# # res = [0] * len(l1)

# postives = []
# negatives = []

# for i in range(len(l1)):
# 	if l1[i] < 0:
# 		negatives.append(l1[i])
# 	else:
# 		postives.append(l1[i])


# if len(postives) > len(negatives):
# 	for i in range(len(negatives)):
# 		l1[i * 2] = postives[i]
# 		l1[(i * 2) + 1] = negatives[i]

# 	for i in range(len(negatives),len(postives)):
# 		l1[i] = postives[i]
# else:
# 	for i in range(len(postives)):
# 		l1[i * 2] = postives[i]
# 		l1[(i * 2) + 1] = negatives[i]

# 	for i in range(len(postives),len(negatives)):
# 		l1[i] = negatives[i]

# print(l1)		

# Time complexity: worst case : O(2N), best case : O(N)
#Space Complexity : O(N)
		

		



		









		




		








