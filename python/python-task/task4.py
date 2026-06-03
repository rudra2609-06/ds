'''

###`Q1:` Join Tuples if similar initial element
While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

For eg.
```
Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
```

'''

# test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

# output = {}

# #  += on tuples means concatenation, NOT addition!

# for tup in test_list:
# 	key = tup[0]
# 	if key in output:
# 		output[key] += tup[1:]
# 	else:
# 		output[key] = tup

# print(list(output.values()))


'''

###`Q2:` Multiply Adjacent elements (both side) and take sum of right and left side multiplication result.


For eg.
```
The original tuple : (1, 5, 7, 8, 10)
Resultant tuple after multiplication :

(1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

output-(5, 40, 91, 136, 80)
```

'''

# t1 = (1, 5, 7, 8, 10)

# output = ()

# i = 0

# while i < len(t1):
# 	if(i < 1):
# 		output += (t1[i] * t1[i+1],)
# 		i+=1
# 	elif i == len(t1) - 1:
# 		output += (t1[i]*t1[i - 1],)
# 		i+=1
# 	else:
# 		p1 = t1[i] * t1[i - 1]
# 		p2 = t1[i] * t1[i + 1]
# 		output += (p1 + p2,)
# 		i+=1


# print(output)

'''

###`Q3`: Check is tuples are same or not?
Two tuples would be same if both tuples have same element at same index
```
t1 = (1,2,3,0)
t2 = (0,1,2,3)

t1 and t2 are not same
```

'''

# t1 = (1,2,3,0)
# t2 = (0,1,2,3)

# isSame = True


# for x,y in zip(t1,t2):
# 	if x != y:
# 		isSame = False
# 		break

# print(isSame)

'''

###`Q4`: Count no of tuples, list and set from a list
```
list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

```
`Output:`

```
List-2
Set-2
Tuples-1
```

'''

# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

# listCount = 0
# setCount = 0
# tupleCount = 0

# for item in list1:
# 	if isinstance(item,tuple):
# 		tupleCount += 1
# 	elif isinstance(item,list):
# 		listCount += 1
# 	else:
# 		setCount += 1

# print(listCount)
# print(setCount)
# print(tupleCount)

# -------------- SETS ---------------

'''

###`Q1:` Write a program to find set of common elements in three lists using sets.
```
Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output : [80, 20]
```

'''

# ar1 = [1, 5, 10, 20, 40, 80]
# ar2 = [6, 7, 20, 80, 100]
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


# output = list(set(ar1) & set(ar2) & set(ar3))

# print(output)

'''

###`Q2:` Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.

`Input:`
```
Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
```
`Output:`
```
No of unique vowels-6
```

'''

# Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

# uniques = set()

# vowels = {'A','E','I','O','U','a','e','i','o','u'}

# for char in Str1:
# 	if char in vowels:
# 		uniques.add(char)

# print(len(uniques))


'''

### `Q3:` Write a program to Check if a given string is binary string of or not.

A string is said to be binary if it's consists of only two unique characters.

Take string input from user.

```
Input: str = "01010101010"
Output: Yes

Input: str = "1222211"
Output: Yes

Input: str = "Campusx"
Output: No
```

'''

# str1 = "01010101010"
# # str1 = "rudra"
# isBinary = True

# uniques = set()

# for char in str1:
# 	uniques.add(char)

# if len(uniques) > 2:
# 	isBinary = False

# print(isBinary)


'''

### `Q4`: find union of n arrays.

**Example 1:**

Input:
```bash
[[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]
```

Output:

```bash
[1, 2, 3, 4, 5, 6, 7, 9]
```

'''

# arr1 = [
#  [1, 2, 2, 4, 3, 6],
#  [5, 1, 3, 4],
#  [9, 5, 7, 1],
#  [2, 4, 1, 3]
# ]

# union_arr = set()

# for elements in arr1:
# 	union_arr |= set(elements)
	
# print(list(union_arr))

'''

### `Q5`: Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using **list-comprehension**.

**Example 1:**

Input:
```bash
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
```

Output:
```bash
[9, 10, 4, 5]
```

**Example 2:**

Input:
```bash
lst1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}
lst2 = {9, 9, 74, 21, 45, 11, 63, 28, 26}
```

Output:
```bash
[9, 11, 26, 28]
```

'''

# lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
# lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}

# print(intersection_list)
# intersection_list = [element for element in lst1 if element in lst2]

# -------------- Dictionary ---------------

'''

### `Q1`: Key with maximum unique values

Given a dictionary with values list, extract key whose value has most unique values.

**Example 1:**

Input:

```bash
test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
```

Output:
```bash
CampusX
```

**Example 2:**

Input:
```bash
test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
```

Output:
```bash
Best
```

'''

# test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}

# uniques = {}

# for elements in test_dict:
# 	length = len(set(test_dict[elements]))
# 	uniques[length] = elements
	
# print(uniques[max(uniques)])

'''

### `Q2`: Replace words from Dictionary. Given String, replace it's words from lookup dictionary.

**Example 1:**

Input:

```bash
test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
```

Output:

```bash
CampusX is the best channel for Data-Science students.
```

**Example 2:**

Input:
```bash
test_str = 'CampusX best for DS students.'
repl_dict = {"good" : "is the best channel", "ds" : "Data-Science"}
```

Output:
```bash
CampusX best for DS students.
```

'''

# test_str = 'CampusX best for DS students.'
# repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

# output =  test_str

# for items in repl_dict:
# 	print(items,repl_dict[items])
# 	if items in test_str:
# 	        output = output.replace(items,repl_dict[items])
		
# print(output)
		
'''

### `Q3`: Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.

**Example 1:**

Input:
```bash
test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]
```

Output:

```bash
[{'name': 'DataScience', 'id': 3}, {'name': 'is', 'id': 8}]
```

**Example 2:**

Input:
```bash
test_list = ["CampusX", 10]
key_list = ["name", "id"]
```

Output:

```bash
[{'name': 'CampusX', 'id': 10}]
```

'''

# test_list = ["DataScience", 3, "is", 8]
# key_list = ["name", "id"]

# output = []

# i = 0
# j = 0

# while i < len(test_list) and j < len(key_list):
#         sample_dict = {}
#         sample_dict[key_list[i]] = test_list[j]
#         output.append(sample_dict)
#         i+=1
#         j+=1

# print(j)

# j = 0
# while i < len(test_list):
#      sample_dict = {}   
#      sample_dict[key_list[j]] = test_list[i]
#      output.append(sample_dict)
#      j+=1
#      i+=1

# print(output)


'''

### `Q4`: Convert a list of Tuples into Dictionary.

**Example 1:**

Input:
```bash
[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
```

Output:
```bash
{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
```

**Example 2:**

Input:
```bash
[('A', 1), ('B', 2), ('C', 3)]
```

Output:
```bash
{'A': [1], 'B': [2], 'C': [3]}
```

'''

list1 = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]

# dict1 = {}

# dict1 = {each_tuple[0]:[each_tuple[1]] for each_tuple in list1}

# dict1 = {x:[y] for x,y in list1} #directly unpacks from list

# for each_tuple in list1:
#         dict1[each_tuple[0]] = [each_tuple[1]]

# print(dict1)

'''

### `Q5`: Sort Dictionary key and values List.

**Example 1:**

Input:

```bash
{'c': [3], 'b': [12, 10], 'a': [19, 4]}
```

Output:

```bash
{'a': [4, 19], 'b': [10, 12], 'c': [3]}
```

**Example 2:**

Input:

```bash
{'c': [10, 34, 3]}
```

Output:

```bash
{'c': [3, 10, 34]}
```

'''

# dict1 = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

# print(sorted(dict1))

# output = {}

# output = {key:sorted(dict1[key]) for key in sorted(dict1.keys())}

# print(output)

