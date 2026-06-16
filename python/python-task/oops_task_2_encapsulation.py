import random
import datetime
from dateutil.relativedelta import relativedelta

'''

###`Q1:`Count number of instances of a class created in Python?

Example:
Say `Car` is any class.
```
maruti = Car()
bmw = Car()
honda = Car()
```
So after creating above instances. We want to count how many instances are created of Car class.

For above example `no of instances = 3`.

Write a program for above problem.

'''


# class Car:
# 	car_instance_count = 0
# 	def __init__(self):
# 		self.count = Car.car_instance_count
# 		Car.car_instance_count += 1


# maruti = Car()
# bmw = Car()
# honda = Car()

# print(f"Number of instance:{Car.car_instance_count}")

'''

###`Q-2:` Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

* The `Deck` class should have a deal method to deal a single card from the deck
* After a card is dealt, it is removed from the deck.
* There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
* The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

`Deck` Class
* It is class of all possible cards in a deck. Total 52 cards.
* Methods - `deal()` it will take out one card from the deck of cards.
* Deck of cards should get shuffeled while creating the deck object.
* `no of cards remaining in deck - <number>` should dsiplay on printing any deck object.

`Card` class
* It is a class of card
* Atrributes - `suit` and `value`
* `<suit> of <value>` should dsiplay on printing any card object.

'''

# class Card:

# 	def __init__(self,suit_input,value_input):
# 		self.suit = suit_input
# 		self.value = value_input
# 	def __str__(self):
# 		return f"{self.suit} of {self.value}"


# class Deck:

# 	suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
# 	def __init__(self):
# 		self.cards = []
# 		for each_suit in self.suit:
# 			for each_value in range(1,14):
# 				if each_value == 10:
# 					each_value = 'J'
# 				if each_value == 11:
# 					each_value = 'Q'
# 				if each_value == 12:
# 					each_value = 'K'
# 				if each_value == 1:
# 					each_value = 'A'
# 				card = Card(each_suit,each_value)
# 				self.cards.append(card)

# 		self.shuffle_cards()


# 	def shuffle_cards(self):
# 		random.shuffle(self.cards)

# 	def deal(self):
# 		return self.cards.pop()
	
# 	def __str__(self):
# 		return f"Number of cards remaining in deck = {len(self.cards)}"



'''

### `Q-4`: Problem 4

**Statement:** Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.

'''

# class ExpiryCalculation:

# 	def __init__(self,manufacturing_date_input,expiry_date_input):
# 		self.manufacturing_date =manufacturing_date_input
# 		self.expiry_date = expiry_date_input

# 	def displays_expiry_date_details(self):
# 		# expiry_day_remaining= manufacturing_date - expiry_date
# 		self.manufacturing = datetime.datetime.strptime(self.manufacturing_date, "%Y-%m-%d").date()
# 		self.expiry = datetime.datetime.strptime(self.expiry_date, "%Y-%m-%d").date()
# 		difference = relativedelta(self.expiry,self.manufacturing)
# 		print("Years left: ",difference.years)
# 		print("Months left: ",difference.months)
# 		print("Days left: ",difference.days)


# e1 = ExpiryCalculation("2000-08-12","2002-09-13")
# e1.displays_expiry_date_details()

'''
Question - 5
'''

# class Student:

# 	__student_id = None

# 	def __init__(self):
# 		self.__student_id = Student.__student_id
# 		Student.__student_id = random.randint(1,1000)
# 		self.__marks = 0
# 		self.__age = 0


# 	def set_marks(self,marks):
# 		self.__marks = marks

# 	def set_age(self,age):
# 		self.__age = age


# 	def get_marks(self):
# 		return self.__marks
	
# 	def get_age(self):
# 		return self.__age

# 	def validate_marks(self):
# 		if self.__marks >=0 and self.__marks <= 100:
# 			return True
# 		else:
# 			return False
	
# 	def validate_age(self):
# 		if self.__age > 20:
# 			return True
# 		else: 
# 			return False
	
# 	def check_qualification(self):
# 		isDataValid = self.validate_age() and self.validate_marks()
# 		if isDataValid:
# 			if self.__marks >= 65:
# 				return True
# 			else:
# 				return False
# 		else:
# 			return False


# s1 = Student()	
# s1.set_age(30)
# s1.set_marks(70)
# print(s1.check_qualification())
# print(s1.get_marks())
# print(s1.get_age())


'''
###`Q-6:` Ice-Cream Scoops and Bowl shop

1. Create a class `Scoop` which has one public property `flavor` and one private proptery `price`. Take `flavor` values during object creation.
2. Create a class `Bowl` with private prperty `scoop_list` which will have list of scoopd object.
3. Create a method `add_scoops` in `Bowl` class which will add any no of `Scoop` objects given as parameter and store it in `scoops_list`.
4. Make getter and setter method for `price` property.
5. Make a method `display` to display `flavour` and `price` of each `Scoop` in `scoop_list` and print total price of the bowl by adding all flavour scoops prices.

6. Make a method `sold` in both `Scoop` class and `Bowl` class to print no of quantity sold.
'''


'''
###`Q-7:`Ice-Cream Bowl continue..

Making advancement in the above classes. `Scoop` and `Bowl`
1. Introduce a property `max_scoops` in `Bowl` class to signify maximum scoops that a bowl can have, exceeding that it will display `Bowl is full`. Take default value as `3`.

2. `no_of_scoop` in `Scoop` class with default value of `1`

3. Print `<flavour> added` with every scoop added.
'''

class Scoop:

	__count = 1
	def __init__(self,flavour_input):
		Scoop.__count += 1
		self.flavour = flavour_input
		self.__sold = Scoop.__count
		self.__price = ''

	def set_price(self,price):
		self.__price = price
	
	def get_price(self):
		return self.__price
	
	def sold(self):
		print("No of quantity sold:",self.__sold)



class Bowl:
	__count = 1
	def __init__(self,maximum_scoop_input = 3):
		Bowl.__count += 1
		self.__sold = Bowl.__count
		self.__scoop_list = []
		self.maximum_scoops = maximum_scoop_input

	def add_scoops(self,*scoop_obj):
		for each_scoop in scoop_obj:
			if len(self.__scoop_list) < self.maximum_scoops:
				self.__scoop_list.append(each_scoop)
				print(f"{each_scoop.flavour} added")
			else:
				print('Maximum Scoops reached')

	def display(self):
		sum = 0
		for each_scoop_obj in self.__scoop_list:
			sum += int(each_scoop_obj.get_price())
			print(f"{each_scoop_obj.flavour}->{each_scoop_obj.get_price()}")

		print("Total Price:",sum)
	def sold(self):
		print("No of quantity sold:",self.__sold)


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('fruit and nut')
b1 = Bowl(1)
b1.add_scoops(s1,s2,s3)
s1.set_price(100)
s2.set_price(200)
s3.set_price(300)
b1.display()
b1.sold()

	
