# Given an integer array nums, find the subarray with the largest sum, and return its sum


l1 = [-2,-3,4,-1,-2,1,5,-3]


# ------------ Brute Force Approach ----------------



# max_sum = float('-inf')
# for i in range(len(l1)):
# 	for j in range(i,len(l1)):
# 		sum_of_sub_array = 0
# 		for k in range(i,j + 1):
# 			sum_of_sub_array += l1[k]
# 		max_sum = max(sum_of_sub_array,max_sum)
	
# print(max_sum)

# Time-Complexity: approx O(N3)
# space-complexity: O(1)


# --------- Better Approach -----------
		
# max_sum = float('-inf')
# for i in range(len(l1)):
# 	sum_of_sub_array = 0
# 	for j in range(i,len(l1)):
# 		sum_of_sub_array += l1[j]
# 		max_sum = max(sum_of_sub_array,max_sum)

# print(max_sum)

# Time-Complexity: approx O(N2)
# space-complexity: O(1)
		

# ---------- Optimal Approach ----------

max_sum = l1[0]  # max sum ending at current element
res = l1[0]      # overall result
startIndex = -1
endIndex = -1

for i in range(1, len(l1)):
    if max_sum < 0:
        max_sum = l1[i]   # fresh start from current element
		# startIndex = i
    else:
        max_sum += l1[i]  # extend previous subarray
    
    res = max(res, max_sum)  # update overall result
	# endIndex = i

print(res)

# Time-Complexity: approx O(N)
# space-complexity: O(1)   

		
		






		
