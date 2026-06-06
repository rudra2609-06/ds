#without return statement


# def is_even(num):
# 	if num % 2 == 0:
# 		print("true")
# 	else:
# 		print("false")
		

# print(is_even(5))
#true
#None

#even if we don't return from any fn then too python sends return which is equal to None 


# L = [1,2,3]
# print(L.append(4)) #now L appends 4 but print is fn and L.append() does not returns anything therefore it will print None


#variable scope

#------------------------------------------------------------------------------

# def g(y):
# 	print(x)
# 	print(x + 1)

# x = 5
# g(x)
# print(x)

'''
Step Procedure:
1.Python Interpreter reaches to def it ignores that and directly searchs for that fn call
2.Before fn call in our code we have a var in global scope and that get's registered 
3. And then interpretor gets the fn call g(x) and then it jumps to fn definition after registering for var and fn
4.Now x is the global scope variable therefore we can access it inside fn therefore it will print 5 and 6
5.After that we are printing again x therefore 5
5
6
5
'''

#------------------------------------------------------------------------------

# def f(y):
# 	x = 1
# 	x += 1
# 	print(x)

# x = 5
# f(x)
# print(x)
# 2, 5

#------------------------------------------------------------------------------

# def h(y):
# 	x += 1 

# x = 5
# h(x)
# print(x)

# When Python sees an assignment to x inside a function, it treats x as a local variable. But before assigning to it, x += 1 needs to read its current value. Since the local x has not been initialized, Python raises:
# UnboundLocalError: local variable 'x' referenced before assignment


#------------------------------------------------------------------------------

# def f(x):
# 	x = x + 1
# 	print('in f(x):x = ',x)
# 	return x

# x = 3
# z = f(x)
# print('in main program scope: z = ',z)
# print('in main progam scope: x = ',x)
#4,4,3

#------------------------------------------------------------------------------

# def f():
# 	def g():
# 		print("inside fn g")
# 	print("inside fn f")

# f()
#"inside fn g" only because we do not have called g() internally


#------------------------------------------------------------------------------

# def g(x):
# 	def h():
# 		x = 'abc'
# 	x = x + 1
# 	print('in g(x): x = ',x)
# 	h()
# 	return x

# x = 3
# z = g(x)
# # 4


