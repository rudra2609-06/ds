import functools

# fn that either accepts fn as input or returns fn as output

def square(x):
	return x**2


#HOF
def transform(f,L):
	output = []
	for i in L:
		output.append(f(i))
	print(output)


# transform(square,[1,2,3])
# transform(lambda x : x**2,[1,2,3])
# transform(lambda x : x**3,[1,2,3])



# Map(lamdafn,iterable) returns iterable

#square the item for list
# l1 = [1,2,3,4]

# res = map(lambda x : x**2,l1)
# print(list(res))


# odd/even labelling of list items
# l1 = [1,2,3,4]
# res = map(lambda x : "odd" if x % 2 != 0 else "even",l1)
# print(list(res))


# fetch names from list of dictionary

# users = [
# 	{
# 		'name':'Rahul',
# 		'age' : 20,
# 		'gender' : 'male'
# 	},
# 	{
# 		'name':'Ansh',
# 		'age' : 16,
# 		'gender' : 'male'
# 	},
# 	{
# 		'name':'Rudra',
# 		'age' : 19,
# 		'gender' : 'male'
# 	}
# ]

# names = map(lambda x : x["name"],users)
# print(list(names))


#filter(fn,iterable) returns iterator

# numbers greater that 5
# l1 = [1,2,3,4,5]

# res = filter(lambda x : x > 5,l1)
# print(list(res))

#fetch fruits start with 'a'

# l1 = ['apple','banana','mango','aam']

# res = filter(lambda fruit : fruit[0] == 'a',l1)
# print(list(res))


#reduce : import from functools module

#sum of all items
# res = functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
# print(res)

# find minimum number
# l1 = [1,2,3,4]
# res = functools.reduce(lambda x,y:x if x < y else y,l1)
# print(res)
