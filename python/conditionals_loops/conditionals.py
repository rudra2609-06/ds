# email = 'rudra@gmail.com'
# password = '1234'


# entered_email = input('Enter email: ')
# entered_password = input('Enter password: ')

# # if entered_email != email or password != entered_password:
# # 	print('Email Or Password is Incorrect')	
# # else:
# # 	print('Login Successfull')


# # modification

# if entered_email != email:
# 	entered_email = input('Enter Email Again 1st chance: ')
# 	if entered_email == email:
# 		print('Welcome')
# 	else:
# 		print('Incorrect,You loosed your chance')
# elif entered_password != password:
# 	entered_password = input('Enter Password Again 1st chance: ')
# 	if entered_password == password:
# 		print('Welcome')
# 	else:
# 		print('Incorrect,You loosed your chance')
# else:
# 	print('You entered correct details in one go')

#find min of 3 input 

a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))

min = None

if b < a and b < c :
	min = b 
elif c < a : 
	min = c
else:
	min = a

print('min is:',min)



