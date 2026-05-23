import keyword
print(keyword.kwlist)

# in python there are total 35 keywords and 4 soft words


# variable name , class name , function name created by programmer is known as identifier

#rules for creating identifier

#cannot start with number
#in special character you can use only underscore
#identifiers cannot be keywords
#cannot use spaces to seperate name of identifier use underscore

#value stored in variable is literal

a = 2
# a is identifier = is operator and 2 is literal

b = 0b1010
#binary literal
print(b)

o = 0o310
#octal representation
print(o)

h = 0x12c
#hexadecimal representation
print(h)

r = 2 + 3j
print(r.real + r.imag)
print(r.real , r.imag)


#python treats boolean as numbers True -> 1 False -> 0

print(True + 5) #-> 6 
print(False + 5) #-> 5

a = None #no value 
print(a)

#if you want to declare variable first and then assign value after in the program you can use None first as literal while declaring a variable

num1 = None

num1 = int(input('Enter number one: '))
print(num1)