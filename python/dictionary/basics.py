#Dictionary is a data structure that stores information in key-value pairs. While keys must be unique and immutable (like strings or numbers), values can be of any data type, whether mutable or immutable. This makes dictionaries ideal for accessing data by a specific name rather than a numeric position like in list.

#characteristics

# Mutable
# keys should only be unique
# key's can't be mutable
# no meaning of indexing here


# ---------- creating dictionary ----------

# empty dictionary

# d1 = {}

#1d

# d2 = {
# 	'name' : 'rudra',
# 	'age' :23
# }

# 2d

# student = {
# 	'name' : 'rudra',
# 	'college':'xyz',
# 	'semester' : 4,
# 	'subjects' : {
# 		'maths' : 50,
# 		'networking' : 30
# 	}
# }

# print(student)

# type conversion
# d4 = dict([(1,1),(2,2),('name','rudra')]) #we are passing list of tuple as key value pair

# print(d4)

#duplicate keys

# d5 = {
# 	'name' : 'nitish',
# 	'name' : 'rudra'
# } #in key's duplicate case last one will be considered

# print(d5)

# mutable items as keys

# d6 = {
# 	'name' : 'nitish',
# 	[1,2,3] : 'rudra'
# }

# print(d6) #error


# ---------- accessing elements dictionary ----------

# my_dict = {'name': 'rudra','age': 19}

# print(my_dict['age'])
# print(my_dict.get('name'))

# ---------- adding key-value pair dictionary ----------

# my_dict = {'name': 'rudra','age': 19}

# my_dict['gender'] = 'male'

# print(my_dict)

# ---------- removing key-value pair dictionary ----------

# my_dict = {'name': 'rudra','age': 19}

#pop

# my_dict.pop('name')
# print(my_dict)

#popitem

# my_dict.popitem() #deletes last key-value pair
# print(my_dict)

#del 
# del my_dict
# print(my_dict) #error as dict deleted

# del my_dict['name']
# print(my_dict)

# clear

# my_dict.clear()
# print(my_dict)

# ---------- editing key-value pair dictionary ----------

student = {
	'name' : 'rudra',
	'college':'xyz',
	'semester' : 4,
	'subjects' : {
		'maths' : 50,
		'networking' : 30
	}
}

# student['semester'] = 3
# print(student)

# student['subjects']['maths'] = 55
# print(student)




