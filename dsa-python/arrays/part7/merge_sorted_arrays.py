# you are given two "sorted" array's such that you need to do in-place replacement within the subarrays such that output should overall contain lesser value elements in first and greater in second

arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]


# ------------- Brute Force Approach -------------

# s1 = len(arr1) - 1
# s2 = len(arr2) - 1

# arr3 = []

# i = 0
# j = 0

# while i <= s1 and j <= s2:
# 	if arr1[i] >= arr2[j]:
# 		arr3.append(arr2[j])
# 		j += 1
# 	else:
# 		arr3.append(arr1[i])
# 		i += 1

# # if j is still lesser than s2
# if j <= s2:
# 	while j <= s2:
# 		arr3.append(arr2[j])
# 		j += 1
# if i <= s1:
# 	while i <= s2:
# 		arr3.append(arr2[i])
# 		i += 1

# print(arr3)

# # replace first arr elements

# for i in range(len(arr3)):
# 	if i <= s1:
# 		arr1[i] = arr3[i]
# 	else:
# 		# this is done because in order to get actual answer i need to subtract it with s1 and i did s1 = len(arr1) - 1 so i needed that 1 here
# 		arr2[i - (s1 + 1)] = arr3[i]

# print(arr1)
# print(arr2)

# TC : O(n + m) + O(n + m)
# SC : O(n + m)

# ------------- Optimal Approach -------------

# i = len(arr1) - 1
# j = 0
# print(min(len(arr1),len(arr2)))

# while i >= j:
# 	if arr1[i] >= arr2[j]:
# 		arr1[i],arr2[j] = arr2[j],arr1[i]
# 		i -= 1
# 		j += 1
# 	else:
# 		break

# print(sorted(arr1))
# print(sorted(arr2))

# TC : O(min(n,m))+O(nlogn)+O(mlogm)
# Sc : O(n + m)




