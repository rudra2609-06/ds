# after learning oop a programmer can create's its own data type

# class : class is a blueprint, class name usually kept in Pascal Case: HelloWorld
# built-in classes : list,tuple,etc
#user -defined classes

# object : object is instance of this class

# banking system

# class Atm:

# 	def __init__(self):
# 		self.pin = ''
# 		self.balance = 0
# 		self.menu()


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
# 			self.check_balance( )
# 		elif user_input == '4':
# 			#withdraw
# 			self.withdraw_money()
# 		else:
# 			exit()
	
# 	def create_pin(self):	
# 		user_pin = input("Enter Your Pin: ")
# 		self.pin = user_pin
# 		user_balance = int(input("Enter Balance: "))
# 		self.balance = user_balance
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
# 			print(f"Your Balance is: {self.balance}")
# 			self.menu()	
# 		else:
# 			print("Incorrect Pin")
# 			self.menu()

# 	def withdraw_money(self):
# 		curr_pin = input("Enter Pin: ")
# 		if self.pin == curr_pin:
# 			amount_to_withdraw = int(input("Enter Amount to withdraw: "))
# 			if self.balance >= amount_to_withdraw:
# 				print("Amount Withdraw Successfully")
# 				self.balance -= amount_to_withdraw
# 				self.menu()
# 			else:
# 				print("Insufficient funds")
# 				self.menu()				
# 		else:
# 			print("Incorrect Pin")
# 			self.menu()


# obj = Atm()


# magic method or dunder method: __name__()
#they have a super power which is whenever you create an object of that class that particular method get's called you need not to call it seperately
#one of which is constructor

# why do we require constructor?
# so constructor is first of all the fn that executes/triggers automatically so we need to write some fn that should get trigger automatically and not by user choice for example connecting to data base and asking to connect to internet in order to run application.Connecting backend also 


# ----------- creating fraction data type -------------

# class Fraction:

# 	def __init__(self,x,y):
# 		self.numerator = x
# 		self.denominator = y

# 	# whenever we put obj of any class inside print fn than python executes code inside str in order to tell user how object looks
# 	def __str__(self):
# 		return f"{self.numerator}/{self.denominator}"

# 	# this is triggered automatically when we add objects of same class using + operand first object is called self and second obj is called other
# 	def __add__(self,other):
# 		new_num = self.numerator * other.denominator + other.numerator * self.denominator
# 		new_deno = self.denominator * other.denominator
# 		return f"{new_num}/{new_deno}"
	
# 	def __sub__(self,other):
# 		new_num = self.numerator * other.denominator - other.numerator * self.denominator
# 		new_deno = self.denominator * other.denominator
# 		return f"{new_num}/{new_deno}"
	
# 	def __mul__(self,other):
# 		new_num = self.numerator * other.numerator
# 		new_deno = self.denominator * other.denominator
# 		return f"{new_num}/{new_deno}"
	
# 	def __truediv__(self, other):
# 		new_num = self.numerator * other.denominator
# 		new_deno = self.denominator * other.numerator
# 		return f"{new_num}/{new_deno}"

# 	# non-magic methods
# 	def convert_to_decimal(self):
# 		return self.numerator/self.denominator


	
# fr1 = Fraction(3,4)
# fr2 = Fraction(4,5)
# print(fr1.convert_to_decimal())
# print(fr1 + fr2)
# print(fr1 - fr2)
# print(fr1 * fr2)
# print(fr1 / fr2)


# class Point:

# 	def __init__(self,x,y):
# 		self.x_cord = x
# 		self.y_cord = y

# 	def __str__(self):
# 		return f"<{self.x_cord},{self.y_cord}"
	
# 	def euclidean_distance(self,other):
# 		distance = ((other.x_cord - self.x_cord) ** 2 + (other.y_cord - self.y_cord) ** 2) ** 0.5
# 		return round(distance,2)

# 	def distance_from_origin(self):
# 		# distance = ((self.x_cord) ** 2 + (self.y_cord) ** 2) ** 0.5
# 		# return round(distance,2)
# 		# ----------- OR -----------
# 		return self.euclidean_distance(Point(0,0)) #euclidean_distance(self,Point(0,0))
	
# p1 = Point(1,2)
# p2 = Point(2,4)

# print(p1.euclidean_distance(p2)) #py internally call fn like this euclidean_distance(p1,p2)
# print(p2.distance_from_origin())


# class Line:
	
# 	def __init__(self,a,b,c):
# 		self.a = a
# 		self.b = b
# 		self.c = c

# 	def __str__(self):
# 		return f"{self.a}x + {self.b}y + {self.c} = 0"

# 	# if you are given point obj and line obj tell wheather that point lies on that line or not
# 	def check_point_on_line(line,point):
# 		if line.a * point.x_cord + line.b * point.y_cord + line.c == 0:
# 			return "lies on line"
# 		else:
# 			return "does not lies on line"
	
# 	#distance between point and line
# 	def distance_between_point_line(line,point):
# 		shortest_line = abs(line.a * point.x_cord + line.b * point.y_cord + line.c)/((line.a ** 2 + line.b ** 2) ** 0.5)
# 		return shortest_line
	
# 	#two lines intersect or not
# 	def check_intersection(line1,line2):
# 		determinant = (line1.a*line2.b) - (line2.a*line1.b)
# 		if determinant != 0:
# 			return "Yes Intersects"
# 		else:
# 			return "No Does Not Intersects"

# l1 = Line(3,4,5)
# l2 = Line(1,-1,0)
# # print(l1.check_point_on_line(Point(1,1)))
# # print(l1.distance_between_point_line(Point(1,1)))
# print(l1.check_intersection(l2))




	




		







