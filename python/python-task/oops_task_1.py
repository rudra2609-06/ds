from math import gcd

'''

##`Q-1:` Rectangle Class
1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

2. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

3. Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

'''



# class Rectangle:

# 	def __init__(self,l,w):
# 		self.length = l
# 		self.width = w
# 		self.peri = 0
# 		self.area = 0

# 	def cal_Area(self):
# 		self.area = self.length * self.width
	
# 	def cal_Perimeter(self):
# 		self.peri = 2 * (self.length + self.width)
	
# 	def diplay(self):
# 		self.cal_Area()
# 		self.cal_Perimeter()
# 		print(f"length of rectangle is: {self.length}")
# 		print(f"Width of rectangle is: {self.width}")
# 		print(f"Perimeter of rectangle is: {self.peri}")
# 		print(f"Area of rectangle is: {self.area}")
	


# my_rectangle = Rectangle(3,4)
# my_rectangle.diplay()


'''

##`Q-2: Bank Class`

1. Create a Python class called `BankAccount` which represents a bank account, having as attributes: `accountNumber` (numeric type), `name` (name of the account owner as string type), `balance`.
2. Create a constructor with parameters: `accountNumber, name, balance`.
3. Create a `Deposit()` method which manages the deposit actions.
4. Create a `Withdrawal()` method  which manages withdrawals actions.
5. Create an `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account.
6. Create a `display()` method to display account details.
Give the complete code for the  BankAccount class.

'''


# class BankAccount:
# 	accountNumber = 0
# 	name = ''
# 	balance = 0
	
# 	def __init__(self,accountNumber,name,balance):
# 		self.accountNumber = accountNumber
# 		self.name = name
# 		self.balance = balance
	
# 	def deposit(self,amount):
# 		self.balance += amount
	
# 	def withdrawal(self,amount):
# 		self.balance -= amount
		
	
# 	def bankFees(self):
# 		print(f"Bank Fees Are {self.balance * 0.05}")
	
# 	def display(self):
# 		print(f"Account Number {self.accountNumber}")
# 		print(f"Account Name: {self.name}")
# 		print(f"Account Balance: {self.balance}")


		
# newAcc = BankAccount(2020021,"Rudra",2800)

# newAcc.withdrawal(200)
# newAcc.deposit(400)
# newAcc.display()


'''

##`Q-3:Computation class`

1. Create a `Computation` class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
2. Create a method called `Factorial()` which allows to calculate the factorial of an integer n. Integer n as parameter for this method

3. Create a method called `naturalSum()` allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

4. Create a method called `testPrime()` in  the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

5. Create  a method called `testPrims()` allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only `1` as their common divisor. Eg. 4 and 9 are prime to each other.



'''

# class Computation:

# 	def __init__(self):
# 		pass

# 	def factorial(self,n):
# 		fact = 1
# 		if n == 1 or n == 0:
# 			print(f"Factorial is {fact}")
# 		fact = 1
# 		while(n != 1):
# 			fact *= n
# 			n -= 1
# 		print(f"Factorial is {fact}")

# 	def naturalSum(n):
# 		if n == 0 or 1:
# 			print("Natural Sum is 1")
# 		else:
# 			sum = 1
# 			while n != 0:
# 				sum += n
# 				n -= 1
# 			print(f"Natural Sum is {sum}")
	
# 	def testPrime(n):
# 		if n == 1:
# 			print("1 is neither Prime nor Composite")
# 		else:
# 			isPrime = True
# 			for i in range(2,int(n ** 0.5) + 1):
# 				if n % i == 0:
# 					isPrime = False
# 					print(f"{n} is not Prime Number")
# 					break
	
# 	def testPrims(n1,n2):
# 		if gcd(n1,n2) == 1:
# 			print("Yes Prime to One Another")
# 		else:
# 			print("Not Prime to One Another")
				
			

				
		

	










	 
		
	
