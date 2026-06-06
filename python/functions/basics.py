# Types of function:
# 1. Built-in fn
# 2. User-defined fn

# def is_even(num):
# 	"""
# 	optional docstring : reading manual of fn what particular fn does
# 	"""
# 	if num % 2 == 0:
# 		return True
# 	else:
# 		return False
	

# res = is_even(4)
# print(res)

# check wheather number is odd or even

# def odd_or_even(num):
# 	"""
# 	this fn accepts num and returns wheather the number is odd or even
# 	input - any valid integer
# 	output - odd/even
# 	created on - 3rd-June-2026
# 	"""
# 	if not isinstance(num,int):
# 		return "Required Integer Input Only"
# 	if num % 2 == 0:
# 		return "even"
# 	else:
# 		return "odd"

# res = odd_or_even(5)
# how to access documentatin for particular fn

# print(odd_or_even.__doc__)
# print(res)


# Types of arguments : Default,Positional and keyword argument

# default argument

# def power(a = 1,b = 1):
# 	return a**b

# res = pow(2,3)

# print(res)


# positional arguments
# power(a,b) #1st argument -> 1st param of fn and 2nd param of fn to 2nd param of fn this is only known as positional arguement


# keyword arguments

# power(b = 2,a = 3)


# -------------- *args and **kwargs ------------------

# above keywords allow us to pass variable number of arguments to a fn

# *args: allow us to pass variable number of non-keywords argument

#for eg: you want to design a fn that accepts n number of inputs and then you return the product of all those numbers

# def multiply(*args):
# 	product = 1
# 	for i in args:
# 		product *= i
# 	print(args) #python internally stores in tuple

# 	return product

# res = multiply(1,2,3,4,5,6)
# print(res)



#**kwargs : allows us to pass any number of keyword arguments
#keyword argument means they contain key-value pair like a dictionary

# def display(**kwargs):
# 	for key,value in kwargs.items():
# 		print(f"{key}-{value}")

# display(india = 'delhi',srilanka = 'colombo')


#Points to remember while using *args and **kwargs

#order of argument matters (normal -> *args -> **kwargs)
# the word agrs and kwargs are just convention you can use any name of choice



