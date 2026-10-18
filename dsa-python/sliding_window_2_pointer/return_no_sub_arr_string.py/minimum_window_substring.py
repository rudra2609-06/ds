# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


s = "ADOBECODEBANC" 
t = "ABC"




# ---------------- Brute Force Approach ----------------
# m = len(s)
# n = len(t)
# res = float('inf')
# resString = ""
# freq = {}

# def matches(window_freq,freq):
# 	for char,needed in freq.items():
# 		if window_freq.get(char,0) < needed:
# 			return False
# 	return True



# for char in range(n):
# 	if t[char] in freq:
# 		freq[t[char]] += 1
# 	else:
# 		freq[t[char]] = 1


# for i in range(m):
# 	window_freq = {}
# 	for j in range(i,m):
# 		if s[j] in window_freq:
# 			window_freq[s[j]] += 1
# 		else:
# 			window_freq[s[j]] = 1

# 		if matches(window_freq,freq):
# 			length = j - i + 1
# 			if length < res:
# 				res = length
# 				resString = s[i:j+1]

# print(resString)

# -------- Optimal Soln --------------

m = len(s)
n = len(t)

need_freq = {}
for each_char_idx in range(n):
	if t[each_char_idx] in need_freq:
		need_freq[t[each_char_idx]] += 1
	else:
		need_freq[t[each_char_idx]] = 1

need = len(need_freq)
have = 0
have_freq = {}

left = 0
res = ""
reslen = float('inf')

for right in range(m):

	if s[right] in have_freq:
		have_freq[s[right]] += 1
	else:
		have_freq[s[right]] = 1
	
	if need_freq.get(s[right]) != None and have_freq[s[right]] == need_freq[s[right]]:
		have += 1
	
	while have == need:
		temp_len = right - left + 1
		if temp_len < reslen:
			res = s[left : right + 1]
			reslen = temp_len
		have_freq[s[left]] -= 1
		if need_freq.get(s[left]) != None and have_freq[s[left]] < need_freq[s[left]]:
			have -= 1
		left += 1
		
print(res)
