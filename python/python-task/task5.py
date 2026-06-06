import math 
import functools
'''

### **`Problem-1:`** Write a Python function that takes a list and returns a new list with unique elements of the first list.

**Exercise 1:**

Input:

```bash
[1,2,3,3,3,3,4,5]
```

Output:

```bash
[1, 2, 3, 4, 5]
```

'''

# def return_unique(l1):
# 	return list(set(l1))

# l1 = [1,2,3,3,3,3,4,5]
# res = return_unique(l1)
# print(res)


'''

### **`Problem-2:`** Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.

**Example 1:**

Input:
```bash
green-red-yellow-black-white
```

Output:
```bash
black-green-red-white-yellow
```

'''


# def sort_and_return(string):
# 	l1 = string.split('-')
# 	sorted_l1 = sorted(l1)
# 	return "-".join(sorted_l1)


# str1 = "green-red-yellow-black-white"
# res = sort_and_return(str1)
# print(res)


'''

### **`Problem 3:`** Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

```
Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
Expected Output :
No. of Upper case characters :  9
No. of Lower case Characters :  47
```

'''

# def count_upper_and_lower_case(string):
# 	count_upper = 0
# 	count_lower = 0
# 	for char in string:
# 		if char.isupper():
# 			count_upper += 1
# 		elif char.islower():
# 			count_lower += 1
# 	return count_upper,count_lower



# str1 = 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
# res = count_upper_and_lower_case(str1)
# print(res)


'''

### **`Problem 4:`** Write a Python program to print the even numbers from a given list.
```
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
```

'''

# def filter_even_numbers(l1):
# 	return [x for x in l1 if x % 2 == 0]


# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = filter_even_numbers(l1)
# print(res)


'''

### **`Problem 5:`** Write a Python function to check whether a number is perfect or not.

A Perfect number is a number that is half the sum of all of its positive divisors (including itself).

Example :

```
The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.

The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
```

'''


# def cal_perfect_number(number):
# 	# first finding all divisors and storing them in a list
# 	divisors = []
# 	for i in range(1,int(math.sqrt(number)) + 1):
# 		if number % i == 0:
# 			divisors.append(i)
# 			if number//i != i:
# 				divisors.append(number//i)
# 	divisors_sum = sum(divisors)
# 	if divisors_sum/2 == number:
# 		return f"Yes {number} is Perfect Number"
# 	else:
# 		print(divisors_sum)
# 		return f"No {number} is not Perfect Number"


# num = 496
# res = cal_perfect_number(num)
# print(res)



'''

### **`Problem-6:`** Write a Python function to concatenate any no of dictionaries to create a new one.

```
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```

'''

# def concatenate_dict(**kwargs):
# 	dict1 = {}
# 	for key,value in kwargs.items():
# 		dict1.update(value)


# 	return dict1

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# res = concatenate_dict(a = dic1, b =  dic2,c = dic3)
# print(res)


'''

`Problem-7` Write a python function that accepts a string as input and returns the word with most occurence.

```
Input:
hello how are you i am fine thank you
```

```
Output
you -> 2
```

'''

# def count_occurency(string):
#     words = string.split()
#     counts = {}

#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

#     word = max(counts, key=counts.get)
#     print(f"{word} -> {counts[word]}")
	

# str1 = "hello how are you i am fine thank you"
# count_occurency(str1)


'''

`Problem-8` Write a python function that receives a list of integers and prints out a histogram of bin size 10

```
Input:
[13,42,15,37,22,39,41,50]
```

```
Output:
{11-20:2,21-30:1,31-40:2,41-50:3}
```

'''

# def calculate_histogram(l1):
# 	histogram = {}
# 	for num in l1:
# 		lower_bound = (num // 10) * 10 + 1
# 		upper_bound = lower_bound + 9
# 		if num % 10 == 0 :
# 			lower_bound = num - 9
# 			upper_bound = num
# 		if f"{lower_bound}-{upper_bound}" not in histogram.keys():
# 			histogram[f"{lower_bound}-{upper_bound}"] = 1
# 		else:
# 			histogram[f"{lower_bound}-{upper_bound}"] += 1
# 	return histogram



# l1 = [13,42,15,37,22,39,41,50]
# res = calculate_histogram(l1)
# print(res)


'''

`Problem-9` Write a python function that accepts a list of 2D co-ordinates and a query point, and then finds the the co-ordinate which is closest in terms of distance from the query point.

```
List of Coordinates
[(1,1),(2,2),(3,3),(4,4)]
Query Point
(0,0)
```

```
Output
Nearest to (0,0) is (1,1)
```

'''

# def calculate_minium_distance(coOrdinates,query):
# 	x1 = query[0]
# 	y1 = query[1]
# 	distance_from_query = {}
# 	for each_ordinate in coOrdinates:
# 		difference = ((each_ordinate[0] - x1)** 2 + (each_ordinate[1] - y1)**2)
# 		distance = math.sqrt(difference)
# 		distance_from_query[each_ordinate] = distance
# 	closest_co_ordinate = min(distance_from_query,key=distance_from_query.get)
# 	return closest_co_ordinate



# coOrdinates = [(1,1),(2,2),(3,3),(4,4)]
# query = (5,5)

# res = calculate_minium_distance(coOrdinates,query)
# print(res)

'''
###`Problem 11:` Write a Python program to add three given lists using Python map and lambda.
'''

# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [7,7,8]

# l4 = map(lambda x,y,z:x+y+z,l1,l2,l3)
# print(list(l4))


'''

###`Problem-12:`Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
`Input:`
```
list1 = [1,2,3,4,5,6]
```
`Output:`
```
[1,2,9,64,625,-]
```

'''

# def calculate_square_raise_to_index(l1):
# 	power_list = []
# 	for i in range(len(l1)):
# 		product = l1[i] ** i
# 		power_list.append(product)
# 	return power_list



# list1 = [1,2,3,4,5,6]
# res = calculate_square_raise_to_index(list1)
# print(res)

'''

###`Problem-13` Using filter() and list() functions and .lower() method filter all the vowels in a given string.

'''

# vowels =  ['a','e','i','o','u']
# str1 = "hi my name is rudra"

# output = filter(lambda char : char.lower() in vowels,str1)
# print(list(output))

'''

`Problem-14`: Use reduce to convert a 2D list to 1D

'''

# two_d_List = [[1,2,3],[4,5,6]]

# # [1,2,3,4,5,6]

# one_d_list = functools.reduce(lambda x,y:x+y,two_d_List)
# print(one_d_list)









