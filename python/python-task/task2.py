'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

# rows = 5

# for i in range(6,1,-1):
# 	for j in range(i - 1,0,-1):
# 		print(j,end=" ")
# 	print()

'''
# Input: data science mentorship program
Output: DSMP
'''

# input = 'data science mentorship program'

# output = [val[0].upper() for val in input.split()]
# print("".join(output))


'''
# Input: str1 = campusx str2 = data
Output : camdatapusx
'''

# str1 = 'campusx'
# str2 = 'data'

# str3 = 'cam{}pusx'.format(str2)
# print(str3)

'''
# Input: PyNaTive
Output: yaivePNT
'''

# str1 = 'PyNaTive'
# str2 = ''

# for i in str1:
# 	if i.islower():
# 		print(i)
# 		str2 += i

# for j in str1:
# 	if j.isupper():
# 		str2 += j

# print(str2)

# ---------- OR ----------

# result = (
# 	''.join(ch for ch in str1 if ch.islower()) +
# 	''.join(ch for ch in str1 if ch.isupper())
# )

# print(result)

# ---------- OR ---------

# filter(function, iterable)
# It's a built-in Python function that works with any iterable (lists, strings, tuples, etc.).

# result1 = ''.join(filter(str.islower,str1)) + "".join(filter(str.isupper,str1))
# print(result1)


'''
# Input: hel12304every093
Output: Sum: 22
Average: 2.75
'''

# str1 = 'hel12304every093'
# total = 0
# count = 0
# average = 0.0

# l = [int(ch) for ch in str1 if ch.isdigit()]

# total = sum(l)
# average = total / len(l)

# print(total)
# print(average)

'''
# Input: 'I am 25 years and 10 months old'
Output: 2510
'''

# str1 = 'I am 25 years and 10 months old'

# res = (''.join(ch for ch in str1 if ch.isdigit()))
# print(res)

'''
Check wheather string is symmetrical
# Input: khokho
Output: True or Entered string is symmetrical
'''

# str1 = 'khokho'
# stri = str1[:len(str1)//2]
# strii = str1[len(str1)//2:]

# if stri == strii:
# 	print("Entered String is symmetrical")
# else:
# 	print("Entered string is unsymmetrical")


'''
Reverse words in given string:
# Input: geeks quiz practice code
Output: code practice quiz geeks
'''

# str1 = 'geeks quiz practice code'
# str_rev1 = ' '.join(word for word in reversed(str1.split(" ")))
# print(str_rev1)

# ---------- OR ---------

# str_rev2 = ' '.join(str1.split()[::-1])
# print(str_rev2)

'''
Filter out uncommon word into the final list
A = "apple banana mango"
B = "banana fruits mango"
Output: ['apple','fruits']
'''

# A = "apple banana mango"
# B = "banana fruits mango"

# a_words = A.split()
# b_words = B.split()

# res = []
# for word in a_words:
# 	if word not in b_words:
# 		res.append(word)

# for word in b_words:
# 	if word not in a_words:
# 		res.append(word)

#----------- OR ---------

# res = [word for word in a_words if word not in b_words] + [word for word in b_words if word not in a_words]

# print(res)

'''
Find location of word in sentence:
# Input: We can learn data science through campusx mentorship program
target : campusx
Output: Location of word is 7
'''

# str1 = 'We can learn data science through campusx mentorship program'
# target = 'campusx'

# words = str1.split()

# res = -1

# for i in range(0,len(words)):
# 	if words[i] == target:
# 		res = i + 1

# print(res)


'''
# Program to remove all duplicate character from string provided through user input
'''

str1 = input("Enter string with duplicate characters not words: ")
res = ''

# for ch in str1:
# 	if ch not in res:
# 		res += ch
# print(res)


# --------- OR ---------

duplicate = False

for i in range(len(str1)):
	duplicate = False

	for j in range(i):
		if str1[i] == str1[j]:
			duplicate = True
			break
	
	if not duplicate:
		res += str1[i]

print(res)