'''
Combine two list index-wise any left-over element will added at last in newList:
l1 = ['M','O','N']
l2 = ['K','E','Y']
l3 = ['M','O','N','K','E','Y']
'''

# l1 = ['M','O','N']
# l2 = ['K','E','Y']

# l3 = []

# # i = 0 
# # j = 0

# # while i < len(l1) and j < len(l2):
# # 	l3.append(l1[i])
# # 	l3.append(l2[j])
# # 	i += 1
# # 	j += 1

# # while i < len(l1):
# # 	l3.append(l1[i])
# # 	i += 1

# # while j < len(l2):
# # 	l3.append(l2[i])
# # 	j += 1

# # print(l3)

# l3 = l1 + l2
# print(l3)

'''
Add 7000 after 6000 in given list:
l1 = [10,20,[300,400,[5000,6000],500],30,40]
l2 = [10,20,[300,400,[5000,6000,7000],500],30,40]
'''

# l1 = [10,20,[300,400,[5000,6000],500],30,40]

# l2 = l1.copy()

# l2[2][2].append(7000)
# print(l2)

'''
candy_list = ['kit kat','jelly belly','double bubble']
no_of_items = [20,40,30]
to print: kit-kat = 20
jelly belly-40
double bubble-30
'''

# candy_list = ['kit kat','jelly belly','double bubble']
# no_of_items = [20,40,30]

# for candy,count in zip(candy_list,no_of_items):
# 	print(f"{candy}-{count}")


'''
add every other number which is greater than curr and also add than number itself
2 then 4+6+10+2 -> 22
l1 = [2,4,6,10,1]
res = [22,20,10,23]
'''
# l1 = [2,4,6,10,1]

# output = []

# output = [curr + sum(x for x in l1 if x > curr) for curr in l1]

# print(output)

'''
list of common unique items in increasing order
l1 = [23,45,67,78,89,34]
l2 = [34,89,55,56,39,67]
res = [34,67,89]
'''

# l1 = [23,45,67,78,89,34]
# l2 = [34,89,55,56,39,67]

# output = []

# output = sorted([curr for curr in l1 if curr in l2])

# print(output)

'''
Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.

`Input:`
```
['1ac21', '23fg', '456', '098d','1','kls']
```

`Output:`
```
['456', '23fg', '1ac21', '1', 'kls', '098d']
'''


# l1 = ['1ac21', '23fg', '456', '098d','1','kls']

# output = []

# products = []

# for word in l1:
# 	product = 1
# 	for ch in word:
# 		if ch.isdigit():
# 			product *= int(ch)
# 	products.append([product,word])

# print(sorted(products,reverse=True))

# for product in sorted(products,reverse=True):
# 	output.append(product[1])

# print(output)

'''
`Problem 8:` Split String of list on K character.

**Example :**

Input:
```bash
['CampusX is a channel', 'for data-science', 'aspirants.']
```

Output:
['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
```
'''

l1 = ['CampusX is a channel', 'for data-science', 'aspirants.']

output = []

# for word in l1:
# 	for sub_word in word.split():
# 		output.append(sub_word)

# print(output)

# output = [sub_wod for word in l1 for sub_wod in word.split()]
# print(output)


'''
### `Problem 9:` Convert Character Matrix to single String using string comprehension.

**Example 1:**

Input:
[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
```

Output:
campux is best channel
'''

# character_matrix = [
# 	['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']
# ]

# outupt = ""

# output = " ".join(''.join(char for char in word) for word in character_matrix)

# print(output)

'''
### `Problem 10:` Add Space between Potential Words.

**Example:**

Input:

```bash
['campusxIs', 'bestFor', 'dataScientist']
```

Output:
```bash
['campusx Is', 'best For', 'data Scientist']
```

'''

l1 = ['campusxIs', 'bestFor', 'dataScientist']

output = []

# for word in l1:
# 	str1 = ''
# 	for ch in word:
# 		if ch.isupper():
# 			str1 += ' ' + ch
# 		else:
# 			str1 += ch
# 	output.append(str1)

# print(output)

# res = [''.join( ' ' + ch if ch.isupper() else ch for ch in word) for word in l1]

# print(res)




