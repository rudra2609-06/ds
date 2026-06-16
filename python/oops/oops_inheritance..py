# aggregation means one class has a class i.e. one class owns the second class for example customer has a address in this customer owns address class


# class Customer:
# 	def __init__(self,name,gender,address):
# 		self.name = name
# 		self.gender = gender
# 		self.address = address

# 	def print_address(self):
# 		print(self.address.city,self.address.state)
	
# 	def edit_address(self,new_name,new_city,new_state):
# 		self.name = new_name
# 		self.address.edit_address(new_city,new_state)


# class Address:
# 	def __init__(self,city,state):
# 		self.city = city
# 		self.state = state

# 	def edit_address(self,new_city,new_state):
# 		self.city = new_city
# 		self.state = new_state


# add1 = Address('navsari','gujarat')
# cust1 = Customer('rudra','male',add1)

# cust1.print_address()

# cust1.edit_address('ansh','surat','gujarat')

# cust1.print_address()



# here in this case we are passing whole address obj to customer so therefore this is the case of aggregation

# if we do __city and make it private then in this case we will not be able to print it we need to pass getter


	
#  ----------------- Inheritance -----------------

# class User:

# 	def __init__(self):
# 		self.name = 'rudra'

# 	def login(self):
# 		print("logged in")

# class Student(User): #(User) tells python this is child class

# 	# def __init__(self,roll_no):
# 	# 	self.roll_no = roll_no
	
# 	def enroll(self):
# 		print('enroll into the course')


# u = User()
# s = Student()

# print(s.name)

# -------------- child class can access --------------
# constructor
# Non-Private Attributes
# Non-Private Methods

#child can't access private members of the class


# ------------ Method Overidding ----------


# class Phone:

# 	def __init__(self,price,brand):
# 		print("Inside phone class")
# 		self.price = price
# 		self.brand = brand
	
# 	def buy(self):
# 		print("phone class")

# class SmartPhone(Phone):

# 	def buy(self):
# 		print("smartphone class")


# s = SmartPhone(20000,'google')

# s.buy()

# if we have method with same name in parent and child child class method will be called provided the object is of childclass

# similar for constructor if we have 2 constructor one for child class and one for parent class in this case if through child object we try create an obj than child class constructor will be called constructor overloading


# ------------------- Super keyword -------------------

# super keyword is used to access parent methods in child class. super keyword is generally used in  class not outside it if used outside it will throw error


# class Phone:

# 	def __init__(self,price,brand):
# 		print("Inside phone class")
# 		self.price = price
# 		self.brand = brand
	
# 	def buy(self):
# 		print("phone class")

# class SmartPhone(Phone):

# 	def buy(self):
# 		print("smartphone class")
# 		# syntax to call parent ka buy method
# 		super().buy()


# s = SmartPhone(20000,'google')

# s.buy()

# super using construtor

# class Phone:

# 	def __init__(self,name,os,price):
# 		print('Inside Phone constructor')
# 		self.name = name
# 		self.os = os
# 		self.price = price


# class SmartPhone(Phone):

# 	def __init__(self,name,os,price,ram,storage):
# 		print('Inside Smartphone constructor')
# 		super().__init__(name,os,price) 
# 		self.ram = ram
# 		self.storage = storage
# 		print('completed Smartphone constructor')


# sm = SmartPhone('apple','ios',20000,'16','128')
# print(sm.os)
# print(sm.price)



# --------- Types Of Inheritance ---------

# single
# multilevel : grandfather -> father -> child
# hierarchical : parent -> all childs
# multiple (diamond) : mother -> child and father -> child
# hybrid: combination of any two other type of inheritance










		