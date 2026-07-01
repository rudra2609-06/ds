# LeetCode Notes:
# Problem: Find all unique quadruplets whose sum is target.
# Idea: Sort the array, fix two numbers, then use two pointers for the other two.
# Trick: Skip duplicates for the first and second fixed numbers to avoid repeated quadruplets.
# Dry run: [1,0,-1,0,-2,2], target=0 -> valid answers include [-2,-1,1,2], [-2,0,0,2], [-1,0,0,1].
# TC and SC: O(N^3) time because two loops plus one two-pointer scan are used, O(1) extra space if output is ignored.

arr = [1,0,-1,0,-2,2]
target = 0

# -------------- Brute Force ---------------

quadraplets = []

# for i in range(len(arr)):
# 	first = arr[i]
# 	for j in range(i + 1,len(arr)):
# 		second = arr[j]
# 		for k in range(j + 1,len(arr)):
# 			third = arr[k]
# 			for l in range(k + 1,len(arr)):
# 				if first + second + third + arr[l] == target:
# 					quadraplet = [first,second,third,arr[l]]
# 					quadraplet = sorted(quadraplet)
# 					if quadraplet not in quadraplets:
# 						quadraplets.append(quadraplet)


# print(quadraplets)

# # TC : O(n5)
# # Sc: O(1)

# --------------------- Optimal Approach --------------------

arr.sort()
for i in range(len(arr)):
	if i > 0 and arr[i - 1] == arr[i]:
		continue
	first = arr[i]
	for j in range(i+1,len(arr)):
		if j > i + 1 and arr[j - 1] == arr[j]:
			continue
		second_pointer = j
		third_pointer = j + 1
		fourth_pointer = len(arr) - 1
		while third_pointer < fourth_pointer:
			total = first + arr[second_pointer] + arr[third_pointer] + arr[fourth_pointer]

			if total < target:
				third_pointer += 1
			elif total > target:
				fourth_pointer -= 1
			else:
				quadraplets.append([first,arr[second_pointer],arr[third_pointer],arr[fourth_pointer]])
				third_pointer += 1
				while third_pointer < fourth_pointer:
					if arr[third_pointer - 1] == arr[third_pointer]:
						third_pointer += 1
					else:
						break
				fourth_pointer -= 1

print(quadraplets)
