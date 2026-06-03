'''
Combine two list index-wise any left-over element will added at last in newList:
l1 = ['M','O','N']
l2 = ['K','E','Y']
l3 = ['M','O','N','K','E','Y']
'''

l1 = ['M','O','N']
l2 = ['K','E']
l3 = []

# i = 0
# j = 0

# while i < len(l1) and j < len(l2):
# 	if(i == j):
# 		l3.append([l1[i],l2[j]])
# 		i+=1
# 		j+=1

# while i < len(l1):
# 	l3.append(l1[i])
# 	i+=1

# while j < len(l2):
# 	l3.append(l2[j])
# 	j+=1

# print(l3)


# --------- OR ---------

# print(list(zip(l1,l2)))

# l3 = [
# 	[a,b] for a,b in zip(l1,l2)
# ] + l1[len(l2):] + l2[len(l1):]

# print(l3)

'''
Add 7000 after 6000 in given list:
l1 = [10,20,[300,400,[5000,6000],500],30,40]
l2 = [10,20,[300,400,[5000,6000,7000],500],30,40]
'''

# l1 = [10,20,[300,400,[5000,6000],500],30,40]

# target = 7000
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

candy_list = ['kit kat','jelly belly','double bubble']
no_of_items = [20,40,30]

# # access elements index-wise
# l1 = [[a,b] for a,b in zip(candy_list,no_of_items)]
# print(l1)

# for item in l1:
# 	print(f'{item[0]}-{item[1]}')

# --------- OR ---------

# for candy, count in zip(candy_list,no_of_items):
# 	print(f'{candy}-{count}')

'''
add every other number which is greater than curr and also add than number itself
2 then 4+6+10+2 -> 22
l1 = [2,4,6,10,1]
res = [22,20,10,23]
'''

# l1 = [2,4,6,10,1]
# res = []

# sum = 0

# for i in range(0,len(l1)):
# 	sum = 0
# 	for j in range(0,len(l1)):
# 		if l1[i] < l1[j]:
# 			sum += l1[j]
	
# 	sum += l1[i]
# 	res.append(sum)

# --------- OR ---------


# res = [x + sum(y for y in l1 if y > x) for x in l1]

# print(res)

'''
list of common unique items in increasing order
l1 = [23,45,67,78,89,34]
l2 = [34,89,55,56,39,67]
res = [34,67,89]
'''

# l1 = [23,45,67,78,89,34]
# l2 = [34,89,55,56,39,67]

# res = sorted([x for x in l1 if x in l2])
# print(res)


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

# l1 = ['CampusX is a channel', 'for data-science', 'aspirants.']

# res = []

# for word in l1:
# 	res += word.split()

# print(res)

'''
### `Problem 9:` Convert Character Matrix to single String using string comprehension.

**Example 1:**

Input:
[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
```

Output:
campux is best channel
'''

# l1 = [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]


# str1 = ''

# str1 = ' '.join(''.join(char for char in word) for word in l1)

# print(str1)



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
res = []

res = [''.join(' ' + ch if ch.isupper() else ch for ch in word) for word in l1]
print(res)




