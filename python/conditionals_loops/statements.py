# break statement is used to exit from the loop
# real life senario: break statement is used while linear searching
for i in range(1,10):
	if(i == 5):
		break
	print(i)

# prime number b/w two given range

lower_range = int(input('Enter lower range: '))
upper_range = int(input('Enter upper range: '))

# 1 to 10
# 2,5,7
is_prime = False
for i in range(lower_range,upper_range + 1):
	if i < 2:
		continue
	elif i == 2:
		print(i)
	for j in range(2,int(i**0.5)+1):
		if i % j == 0:
			is_prime = False
			break
		else:
			is_prime = True
	
	if is_prime:
		print(i)
	
# continue statement skips the currnent iteration if encountered
# real-life senario:- we want to skip the product which is out of stock

# pass is a do-nothing statement in Python. It's used when Python expects a statement syntactically, but you don't want any action to occur yet.

for i in range(1,10):
	pass



