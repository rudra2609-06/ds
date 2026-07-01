# LeetCode Notes:
# Problem: Find all unique triplets whose sum is 0.
# Idea: Sort the array, fix one element, then use two pointers for the other two.
# Trick: Skip duplicate fixed values and duplicate pointer values so triplets do not repeat.
# Dry run: [-1,0,1,2,-1,-4] -> sorted -> answers are [-1,-1,2] and [-1,0,1].
# TC and SC: O(N^2) time because each fixed value uses one two-pointer scan, O(1) extra space if output is ignored.

# you are given an array of integers which can be duplicates and you need to return the triplets(values) which sums upto 0 such that idx should be distinct and triplet should not repeat

arr = [-1,0,1,2,-1,-4]

triplets = []

# -------------------- Brute Force Soln --------------------

# for i in range(len(arr)):
# 	first_element = arr[i]
# 	for j in range(i + 1,len(arr)):
# 		second_element = arr[j]
# 		for k in range(j + 1,len(arr)):
# 			third_element = arr[k]
# 			if first_element + second_element + third_element == 0:
# 				triplet = []
# 				triplet.append(first_element)
# 				triplet.append(second_element)
# 				triplet.append(third_element)
# 				triplet = sorted(triplet)
# 				if triplet not in triplets:
# 					triplets.append(triplet)
# 				break

			   

# print(triplets)

'''
O(n³)        → three loops
× O(n)       → duplicate check inside
+ O(1)       → sorting 3 elements

= O(n⁴)  ← actual complexity!
SC: O(1)
'''

# -------------------- Optimal Soln --------------------

arr.sort()
for i in range(len(arr)):
	first_element = arr[i]
	if i > 0 and arr[i - 1] == arr[i]:
		continue
	second_element_pointer = i + 1
	third_element_pointer = len(arr) - 1
	while second_element_pointer < third_element_pointer:
		total = first_element + arr[second_element_pointer] + arr[third_element_pointer]
		if total < 0:
			second_element_pointer += 1
		elif total > 0:
			third_element_pointer -= 1
		else:
			triplets.append([first_element,arr[second_element_pointer],arr[third_element_pointer]])
			second_element_pointer += 1
			while second_element_pointer < third_element_pointer:
				if arr[second_element_pointer] == arr[second_element_pointer - 1]:
					second_element_pointer += 1
				else:
					break
			third_element_pointer -= 1

print(triplets)




