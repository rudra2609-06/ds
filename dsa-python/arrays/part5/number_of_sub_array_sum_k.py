# you are given an array and you need to find number of subarrays whose sum is equal to k

l1 = [1,2,3,-3,1,1,1,4,2,-3]
k = 3

# so there are 8 total subarray's whose sum is 3
# count = 0

# for i in range(len(l1)):
# 	sum_elements = 0
# 	for j in range(i,len(l1)):
# 		sum_elements += l1[j]
# 		if sum_elements == k:
# 			count += 1



# print(count)

# TC : O(N2)
# SC : O(1)

# ------------ Optimal Solution ---------------


prefix_sum_map = {0: 1}

count = 0
prefixSum = 0
for i in range(len(l1)):
	prefixSum += l1[i]

	if prefix_sum_map.get(prefixSum - k) is not None:
		# how many times it occured
		count += prefix_sum_map[prefixSum - k]
	
	if prefixSum not in prefix_sum_map:
		prefix_sum_map[prefixSum] = 1
	else:
		prefix_sum_map[prefixSum] += 1

print(prefix_sum_map)
print(count)
