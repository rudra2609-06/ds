import json
import pickle

# with use of serialization and de-serialization we can store complex data type into any file with some specific extension

# Serialization: Process of converting python data types to json format
# Deserialization: Process of converting json format to python data type
# use module json

# ----------------- serialization -----------------


# list

# L = [1,2,3,4]

# with open('demo.json','w') as f:
# 	json.dump(L,f)


# dict 

# d = {
# 	'name' : 'rudra',
# 	'age' : 33
# }


# with open('demo.json','w') as f:
# 	json.dump(d,f,indent=4)

# ----------------- deserialization -----------------

# with open('demo.json','r') as f:
# 	print(json.load(f))



# ----------------- Special Case for Tuple -----------------

# t1 = (1,2,3,4,5)

# with open('demo.json','w') as f:
# 	json.dump(t1,f) #it will store it as list

# with open('demo.json','r') as f:
	# print(json.load(f))
	# print(type(json.load(f))) #list



# serializing and deserializing custom objects

# class Person:

# 	def __init__(self,fname,sname,age,gender):
# 		self.fname = fname
# 		self.sname = sname
# 		self.age = age
# 		self.gender = gender


# p1 = Person('rudra','thakkar',40,'male')

# with open('demo.json','w') as f:
# 	json.dump(p1,f) #error

# so if i want to add like "Rudra thakkar 18 male"

# def check_before_serialization(p_obj):
# 	if isinstance(p_obj,Person):
# 		return f"{p_obj.fname} {p_obj.sname} {p_obj.age} {p_obj.gender}"



# we can't serialize other than python data type if we need to serialize them we need to return its info to be stored that return thing could be str,int,dict,list,tuple

# with open('demo.json','w') as f:
# 	json.dump(p1,f,default=check_before_serialization)


# --------- But if i want to serialize whole obj ---------

# --------------- pickling ---------------

# pickling is the process in which python obj is converted into byte stream 
#unpickling is the reverse of it
# we need to use pickle module


# class Person:

# 	def __init__(self,fname,sname,age,gender):
# 		self.fname = fname
# 		self.sname = sname
# 		self.age = age
# 		self.gender = gender

# 	def display_info(self):
# 		print(f"{self.fname}")


# p1 = Person('rudra','thakkar',40,'male')

# pickle dump -> obj to byte stream 

# with open('person_info.pkl','wb') as f:
# 	pickle.dump(p1,f)


# with open('person_info.pkl','rb') as f:
# 	# print(pickle.load(f))
# 	p = pickle.load(f)
# 	p.display_info()


# Pickle vs Json
# pickle for binary
# json for text based human readable format