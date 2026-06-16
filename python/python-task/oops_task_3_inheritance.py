'''
### `Problem-1:` Class inheritence

Create a **Bus** child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.
'''

# class Vehicle:
# 	def __init__(self,seating_capacity):
# 		self.seating_capacity = seating_capacity

# 	def fare(self):
# 		print(f"fare is: {self.seating_capacity * 100}")


# class Bus(Vehicle):

# 	def __init__(self):
# 		super().__init__(50)

# 	def fare(self):
# 		base_fare = self.seating_capacity * 100
# 		print(f"fare is: {base_fare + (base_fare * 0.1)}")


# b1 = Bus()
# b1.fare()

'''
### `Problem-3:` Write a program that has a class Point. Define another class Location which has two objects (Location & Destination) of class Point. Also define a function in Location that prints the reflection of Destination on the x axis.
'''

# class Point:
# 	def __init__(self,x_cordinate,y_cordinate):
# 		self.x = x_cordinate
# 		self.y = y_cordinate


# class Location:

# 	def __init__(self,point_location,point_destination):
# 		self.location = point_location
# 		self.destination = point_destination

# 	def calculate_reflection(self):
# 		print(f'Reflection is: {self.destination.x},{-self.destination.y}')


# location = Point(3,4)
# destination = Point(5,6)
# l1 = Location(location,destination)
# l1.calculate_reflection()


'''
### `Problem-5:` Write a program with class Bill. The users have the option to pay the bill either by cheque or by cash. Use the inheritance to model this situation.
'''

# class Bill:
# 	def __init__(self,payment_method):
# 		self.method = payment_method

# 	def check_payment_method(self):
# 		print(f"Method is: {self.method}")


# class MethodOfPayment(Bill):
# 	def __init__(self,method):
# 		super().__init__(method)


# m1 = MethodOfPayment('cash')
# m1.check_payment_method()



	




