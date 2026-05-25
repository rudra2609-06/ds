# common functions: works on all data types

# note: any of the function in string does not replaces the original string but it creates the new string in memory and then manipulates it and prints it

# len,max,min,sorted(output is list)

print(len('rudra ')) #len also count space
print(max('rudra'))
print(min('rudra'))
print(sorted('rudra')) #by default : ascending
print(sorted('rudra',reverse=True)) 

# only string related functions

# capitalize: converts first character or string to capital
st = 'hello world'

print(st.capitalize())

# title: every word's first letter is capital

print(st.title())

# upper: all char upper case
print(st.upper())

# lower: all char lower case
print(st.lower())

#swap case: upper char -> lower , lower -> upper
s2 = 'heLLo World'
print(s2.swapcase())

# count/find/Index

print('my name is rudra'.count('i'))

print('my name is rudra'.find('is')) #8 if found else -1

# print('my name is rudra'.index('x')) #is found returns index else error similar to find but difference lies in case when substring not found


# endswith/startswith

print('my name is rudra'.endswith('ra')) #True
print('my name is rudra'.startswith('x')) #False

# format: targets the bracket and stores the value

name = 'rudra'
gender = 'male'

print('Hi my name is {} and my gender is {}'.format(name,gender))


# isalnum/isalpha/isdigit/isidentifier

print('rudra'.isalnum())
print('rudra$'.isalnum())

print('rudra'.isalpha()) #checks all alpha not not

print('234'.isdigit()) #checks only digits or not

print('1name'.isidentifier) #checks if it is valid identifier according to python or not


# split/join

# split breaks the words and puts into list
print('hi my name is rudra'.split(" "))
print('hi my name is rudra'.split("i"))


# join : reverse of split in this case we join the words to form a sentence and only join strings not integers

print(" ".join(['rudra','thakkar']))
print("-".join(['rudra','thakkar']))


# replace: replaces particular substring

s3 = "rudra thakkar"
print(s3.replace('rudra','ansh'))

# strip : similar to js trim
name = "ansh            "
print(len(name))
print(len(name.strip()))