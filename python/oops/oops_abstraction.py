from abc import ABC,abstractmethod


# abstract class is a class that contains one or more abstract methods
# it should inherit from ABC class
class BankApp(ABC):

	def dataBase(self):
		print("connected to database")

	@abstractmethod
	def security(self):
		pass

class MobileApp(BankApp):
	
	def mobile_login(self):
		print("login into mobile")

	# we need to add security method if we want to inherit BankApp
	def security(self):
		print("mobile security")


m1 = MobileApp()

m1.dataBase()
