# LeetCode Notes:
# Problem: Count how many subarrays have XOR equal to k.
# Idea: Use prefix XOR and store how many times each prefix XOR has appeared.
# Trick: If pref ^ oldPref = k, then oldPref = pref ^ k, so we search for pref ^ k in the map.
# Dry run: [4,2,2,6,4], k=6 -> matching old prefix XORs add to the answer count.
# TC and SC: O(N) time because each value is processed once, O(N) space because prefix XOR counts are stored.

# you are given an array and you need to find number of subarrays whose xor is equal to k


arr = [4,2,2,6,4]
target = 6

# ----------------- Brute Force Approach -----------------
# count = 0
# for i in range(len(arr)):
# 	j = len(arr) - 1
# 	while j > i:
# 		res_xor = arr[j] ^ arr[i]
# 		if res_xor == target:
# 			count += 1
# 		j -= 1

	
# print(count)

# TC : O(N2)
# SC : O(1)

# ---------------- Optimal Approach ----------------

# prefixXor = 0
# prefixXor_Map = {0:1}
# count = 0
# for i in range(len(arr)):
# 	prefixXor ^= arr[i]

# 	# if prefixXor in map or not
# 	if prefixXor_Map.get(target ^ prefixXor) != None:
# 		count += prefixXor_Map[target ^ prefixXor]
	
# 	if prefixXor not in prefixXor_Map:
# 		prefixXor_Map[prefixXor] = 1
# 	else:
# 		prefixXor_Map[prefixXor] += 1
	
# print(count)

# TC : O(N)
# SC : O(N)
