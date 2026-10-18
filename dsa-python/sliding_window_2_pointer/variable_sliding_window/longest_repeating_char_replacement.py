# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.


s = 'ABCDE'
k = 1
res = 0
n = len(s)

# ------------------ Brute Force Approach ------------------

# if not s:
#     res = 0

# for i in range(n):
# 	freq = {}
# 	for j in range(i,n):
# 		if s[j] not in freq:
# 			freq[s[j]] = 1
# 		else:
# 			freq[s[j]] += 1
# 		max_count = max(freq.values())
# 		wind_len = j - i + 1
# 		if wind_len - max_count <= k:
# 			res = max(res,j - i + 1)
# 		else:
# 			break

# print(res)

# ------------------ Optimal Approach ------------------

# left = 0
# freq = {}
# for right in range(n):

# 	# if not then add else update its freq
# 	if s[right] not in freq:
# 		freq[s[right]] = 1
# 	else:
# 		freq[s[right]] += 1

# 	# cal win_size
# 	win_size = right - left + 1
# 	max_count = max(freq.values())

# 	if win_size - max_count > k:
# 		freq[s[left]] -= 1
# 		left += 1
# 		win_size -= 1
	
# 	res = max(res,right - left + 1)

# print(res)
	

	

