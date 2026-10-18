# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

#  Find the length of the longest substring without repeating characters.

s = "abcabcac"
# ------------- Brute Force --------------

# n = len(s)
# ans = 0
# ansStr = ""
# for i in range(n):
# 	sub = ""
# 	for j in range(i,n):
# 		if s[j] in sub:
# 			break
# 		else:
# 			sub += s[j]
# 	if len(sub) >= ans:
# 		ansStr = sub
# 		ans = len(sub)
# print(ansStr)

			

# ------------ Optimal Sol -----------


# res = [0] * 2
# left = 0
# count = {}
# n = len(s)
# max_len = 0
# length = 0
# for right in range(n):
# 	curr_char = s[right]
# 	if count.get(curr_char) != None:
# 		if left <= count[curr_char]:
# 			left = count[curr_char] + 1
# 	count[curr_char] = right
# 	length = right - left + 1
# 	if length > max_len:
# 		res[0] = left
# 		res[1] = right
# 		max_len = length
	

# print(s[res[0]:res[1] + 1])