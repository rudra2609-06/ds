'''
# Input: data science mentorship program
# Output: DSMP
'''

# str1 =  "data science mentorship program"

# output = ""

# output = "".join(word[0].upper() for word in str1.split())

# print(output)


'''
# Input: str1 = campusx str2 = data
Output : camdatapusx
'''

# str1 = "campusx"
# str2 = "data"

# output = ""

# middle_index = len(str1) // 2

# output = str1[:middle_index] + str2 + str1[middle_index:]
# print(output)


'''
# Input: PyNaTive
Output: yaivePNT
'''

# str1 = "PyNaTive"
# output = ""

# str_lower_case = "".join(char for char in str1 if char.islower())
# str_upper_case = "".join(char for char in str1 if char.isupper())

# output = str_lower_case + str_upper_case
# print(output)


'''
# Input: hel12304every093
Output: Sum: 22
Average: 2.75
'''

# str1 = "hel12304every093"

# summation = 0
# digits_list = []
# count = 0

# digits_list = [int(char) for char in str1 if char.isdigit()]

# summation = sum(digits_list)
# avearge = summation/len(digits_list)


# print(summation)
# print(avearge)


'''
# Input: 'I am 25 years and 10 months old'
Output: 2510
'''

# str1 = 'I am 25 years and 10 months old'

# output = ''

# output = "".join(char for char in str1 if char.isdigit())

# -------- OR ----------

# output = "".join(filter(str.isdigit,str1))

# print(output)


'''
Check wheather string is symmetrical
# Input: khokho
Output: True or Entered string is symmetrical
'''

# str1 = "khokho"

# substr1 = str1[:len(str1)//2]
# substr2 = str1[len(str1)//2:]

# print(substr1 == substr2)


'''
Reverse words in given string:
# Input: geeks quiz practice code
Output: code practice quiz geeks
'''

# str1 = "geeks quiz practice code"

# output = ""

# words = str1.split()
# output = " ".join(words[i] for i in range(len(words)-1,-1,-1))

# ------------ OR -----------

# words = str1.split()
# reversed_words = words[::-1]
# output = " ".join(reversed_words)

# print(output)

# ------------ OR -----------

# output = " ".join(str1.split()[::-1])

# print(output)


'''
Filter out uncommon word into the final list
A = "apple banana mango"
B = "banana fruits mango"
Output: ['apple','fruits']
'''

# A = "apple banana mango"
# B = "banana fruits mango"

# output = []

# output = [fruit for fruit in A.split() if fruit not in B] + [fruit for fruit in B.split() if fruit not in A]

# print(output)


'''
Find location of word in sentence:
# Input: We can learn data science through campusx mentorship program
target : campusx
Output: Location of word is 7
'''

# str1 = "We can learn data science through campusx mentorship program"
# target = "campusx"

# output = ''
# words = str1.split()
# word = "".join(word for word in words if target == word)
# output = words.index(word) + 1
# print(output)

'''
# Program to remove all duplicate character from string provided through user input
'''

# str_input = ''

# str_input = input("Enter string containing duplicate characters: ")

# if not str_input:
# 	print("Enter valid string")
# 	exit()

# result = ''

# result += "".join(ch for ch in str_input if ch not in result)

# print(result)

















