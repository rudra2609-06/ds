# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

s = "aabbcccd"
k = 2

n = len(s)
res = 0

# for i in range(n):
# 	freq = {}
# 	for j in range(i,n):
# 		if s[j] in freq:
# 			freq[s[j]] += 1
# 		else:
# 			freq[s[j]] = 1
# 		if len(freq) > k:
# 			break
# 		else:
# 			res = max(res,j - i + 1)
			


# print(res)


# ------------- Optimal Soln -------------

left = 0
freq = {}
for right in range(n):
	if s[right] in freq:
		freq[s[right]] += 1
	else:
		freq[s[right]] = 1

	while len(freq) > k:
		freq[s[left]] -= 1
		if freq[s[left]] == 0:
			freq.pop(s[left],None)
		left += 1

	win_size = right - left + 1
	res = max(res,win_size)

print(res) 