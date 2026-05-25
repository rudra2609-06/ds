# strings are collection of characters
# In python strings are collection of unicode characters not ascii
# ascii: 2**8
#unicode : 2**16

# --------- creating python strings ---------

n1 = 'rudra'
n2 = "rudra"

# for multi-line strings
n3 = '''rudra'''
n4 = """rudra"""

n5 = str('hello')


# --------- accessing/indexing python strings ---------

# positive indexing: first element from 0
# s = 'hello world'

# print(s[0])
# print(s[1])
# print(s[5]) #white space

# #negative idexing: last element from -1
# print(s[-1])
# print(s[-2])
# print('->',s[-0]) #equals to 0

# --------- slicing python strings ---------

s = 'hello world'

print(s[0:5]) #second param is not included
print(s[0:]) #upto last
print(s[:-1]) #from 0 to -2 as -1 is not included
print(s[:]) #whole string

# with step-size

print(s[0:4:2]) #from 0 to 3 with skipping 2 character


# reverse the given string
print(s[::-1])

#negative indexing with slicing : whenever using negative indexing first param should be greater 
# world
print(s[-5:])

#reverse->world
print(s[:-6:-1])


# --------- editing and deleting python strings ---------

#python strings are immutable which means we can't change them once created

# s1 = 'hello world'

# del s1 #we are deleting not actually roughly 
# del s1[-1:-5:2] #if we try to delete the portion of string than we are editing it that is not possible
# print(s1)  # error because no such s1 exists now


# ----------- operators on string ---------

# + and *
print('delhi' + 'mumbai')
print('delhi' * 5)

# all realational works on string

# print('delhi' == 'mumbai')
print('delhi' < 'mumbai')
print('mumbai' < 'pune') # p comes later than m

# logical operator
'''
remember in python empty string is False and non-empty string is True
so therefore if we do 'delhi' and 'mumbai' both are True and True
that means 1 and 1 which is 1 world will be printed
but if we do '' and 'delhi' than '' is 0 and 'delhi' will be 1
0 and 1 will be 0 so '' will be printed

if we use or than first Truthy word encountered will be printed
'''


print('hello' and 'world')
print('hello' or 'world')
print('' and 'delhi')
print(not '')
print(not 'delhi')


# loops on string

for i in 'hello':
	print(i)

for i in 'delhi':
	print('pune')

# membership operator in and not in

print('D' in 'delhi') #will show False as python is case sensitive as d and D are different



