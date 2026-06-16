# we can create attributes inside class from outside using objects

# class Person:

# 	def __init__(self,name_input,country_input):
		# this name and country are known as instance var such that their value differs from object to object as input changes 
# 		self.name = name_input
# 		self.country = country_input
	
# 	def greet(self):
# 		if self.country.lower() == 'india':
# 			print("Namaste")
# 		else:
# 			print("Hello")


# p1 = Person('rudra','India')

# print(p1.country)
# print(p1.name)
# p1.greet()
# # print(p1.gender) # error : because gender is not present in Person

# p1.gender = 'male'
# print(p1.gender)


# ---------- Reference Variables ----------

# uptil now we were in such a mindset that by doing these p1 = Person() so p1 is the object
#That's not technically correct.To Prove that we can just do Person() and in that case object will be created 
#so ultimately that p1 just holds the reference of that particular obj
# we can assign that p1 to q1 if we want

# class Person:

# 	def __init__(self):
# 		self.name = 'rudra'
# 		self.country = 'india'

# 	def greet(self):
# 		return "hello"
	

# this shows that object is created just by doing Person() and p1 just holds refrence for our ease
# print(Person().greet())



# assinging new variable to existing object does not creates new object it still points to same reference

# p1 = Person()
# q = p1

# q.name = 'ansh'
# print(q.name)
# print(p1.name)



# class Person:

# 	def __init__(self):
# 		self.name = 'rudra'
# 		self.country = 'india'

# 	# This is inside a class therefore it is a method
# 	def greet(self):
# 		return "hello"
	

# this is outside the class therefore it is a function
# def greet(person):
	# print(id(person))
# 	print(f"Hi, my name is {person.name} and I am from {person.country}")


# p1 = Person()
# print(id(p1))
# greet(p1)
#objects are mutable in python


# ---------------- Encapsulation ----------------


# class Atm:

# 	def __init__(self):
# 		self.pin = ''
# 		self.__balance = 0
# 		# self.menu()

# 	def get_balance(self):
# 		return self.__balance
	
# 	def set_balance(self,new_value):
# 		if type(new_value) == int:
# 			self.__balance = new_value
# 			print("successfully updated the balance")
# 		else:
# 			print("Beta bohot marenge")


# 	def menu(self):
# 		user_input = input("""
# 		How Can I help You?
# 		1.Press 1 To create pin
# 		2.Press 2 To change pin
# 		3.Press 3 To check balance
# 		4.Press 4 To withdraw
# 		5.Anything Else To Exit
# 		""")

# 		if user_input == '1':
# 			# create pin
# 			self.create_pin()
# 		elif user_input == '2':
# 			# change pin
# 			self.change_pin()
# 		elif user_input == '3':
# 			# check balance
# 			self.check_balance()
# 		elif user_input == '4':
# 			#withdraw
# 			self.withdraw_money()
# 		else:
# 			exit()
	
# 	def create_pin(self):	
# 		user_pin = input("Enter Your Pin: ")
# 		self.pin = user_pin
# 		user_balance = int(input("Enter Balance: "))
# 		self.__balance = user_balance
# 		print("Pin Created Successfully")
# 		self.menu()
	


# 	def change_pin(self):
# 		curr_pin = input("Enter current pin: ")
# 		if curr_pin == self.pin:
# 			new_pin = input("Enter New Pin: ")
# 			self.pin = new_pin
# 			print("Pin changed successfully")
# 			self.menu()
# 		else:
# 			print("Incorrect Current Pin.Please Try Again")
# 			self.menu()

# 	def check_balance(self):
# 		curr_pin = input("Enter Pin: ")
# 		if self.pin == curr_pin:
# 			print(f"Your Balance is: {self.__balance}")
# 			self.menu()	
# 		else:
# 			print("Incorrect Pin")
# 			self.menu()

# 	def withdraw_money(self):
# 		curr_pin = input("Enter Pin: ")
# 		if self.pin == curr_pin:
# 			amount_to_withdraw = int(input("Enter Amount to withdraw: "))
# 			if self.__balance >= amount_to_withdraw:
# 				print("Amount Withdraw Successfully")
# 				self.__balance -= amount_to_withdraw
# 				self.menu()
# 			else:
# 				print("Insufficient funds")
# 				self.menu()				
# 		else:
# 			print("Incorrect Pin")
# 			self.menu()


# obj = Atm()
# obj.balance = 'hehe'
# print(obj.get_balance()) it will be 0 as we can't change it now
# once we keep double underscore __ before any name of attribute or method inside class we can't change its name from outside through object 

# for example if i do __self.balance python performs name mangling so inside memory it renames it as _Atm__balance i.e. _ClassName__attributeName 

# but still if we use that name we can change the value from outside therefore in python attributes or method are not truly private

# but for some reasons we need that private variable access so in that case we provide access through getters and setters and we make this or each attribute



#  -------------- Collection of objects --------------

# class Person:

# 	def __init__(self,name_input,country_input):
# 		self.name = name_input
# 		self.country = country_input
	
# 	def greet(self):
# 		if self.country.lower() == 'india':
# 			print("Namaste")
# 		else:
# 			print("Hello")


# p1 = Person('rudra','India')
# p2 = Person('ansh','sweden')
# p3 = Person('roni','us')
# p4 = Person('eshani','china')
# p5 = Person('chirag','pakistan')

# L = [p1,p2,p3,p4,p5]

# # print(L)

# for i in L:
# 	print(i.name,i.country)


# d1 = {'p1':p1,'p2':p2}

# for i in d1:
# 	print(d1[i].name)


# -------------- Static Variables --------------

# instance variable is object's particular variable and its value for each obj is independent from other and different from each one

# static variable is class's particular variable and its value it not independent for each object it is shared classname.variable_name while exposing it for some reasons via getter and setter we need not to have that default method argument self as self points to obj and there is not requirement for obj here static var is class based

# static method are those method which can be accessed directly without creating obj of that class

# through analogy:

# if we are making college website than:

# student cgpa: instance variable because it is unique/independent from each other

# student name: instance variable because it is unique/independent from each other 

# college name : static variable because it is same for every student and individual belonging to college


class Atm:

	__counter = 1

	def __init__(self):
		self.pin = ''
		self.__balance = 0
		self.customer_id = Atm.__counter
		Atm.__counter += 1
		# self.menu()


	@staticmethod
	def get_customer_id():
		return Atm.__counter
	
	def set_customer_id(self,new_val):
		self.customer_id = new_val
		

	def get_balance(self):
		return self.__balance
	
	def set_balance(self,new_value):
		if type(new_value) == int:
			self.__balance = new_value
			print("successfully updated the balance")
		else:
			print("Beta bohot marenge")


	def menu(self):
		user_input = input("""
		How Can I help You?
		1.Press 1 To create pin
		2.Press 2 To change pin
		3.Press 3 To check balance
		4.Press 4 To withdraw
		5.Anything Else To Exit
		""")

		if user_input == '1':
			# create pin
			self.create_pin()
		elif user_input == '2':
			# change pin
			self.change_pin()
		elif user_input == '3':
			# check balance
			self.check_balance()
		elif user_input == '4':
			#withdraw
			self.withdraw_money()
		else:
			exit()
	
	def create_pin(self):	
		user_pin = input("Enter Your Pin: ")
		self.pin = user_pin
		user_balance = int(input("Enter Balance: "))
		self.__balance = user_balance
		print("Pin Created Successfully")
		self.menu()
	


	def change_pin(self):
		curr_pin = input("Enter current pin: ")
		if curr_pin == self.pin:
			new_pin = input("Enter New Pin: ")
			self.pin = new_pin
			print("Pin changed successfully")
			self.menu()
		else:
			print("Incorrect Current Pin.Please Try Again")
			self.menu()

	def check_balance(self):
		curr_pin = input("Enter Pin: ")
		if self.pin == curr_pin:
			print(f"Your Balance is: {self.__balance}")
			self.menu()	
		else:
			print("Incorrect Pin")
			self.menu()

	def withdraw_money(self):
		curr_pin = input("Enter Pin: ")
		if self.pin == curr_pin:
			amount_to_withdraw = int(input("Enter Amount to withdraw: "))
			if self.__balance >= amount_to_withdraw:
				print("Amount Withdraw Successfully")
				self.__balance -= amount_to_withdraw
				self.menu()
			else:
				print("Insufficient funds")
				self.menu()				
		else:
			print("Incorrect Pin")
			self.menu()


p1 = Atm()
print(p1.customer_id)

p2 = Atm()
print(p2.customer_id)