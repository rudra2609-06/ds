a,b,c = (1,2,3)
print(a)
print(b)
print(c)


# a,b = (1,2,3,4)
# print(a) #error too many values to unpack 

a,b,*others = (1,2,3,4)
print(a) #1
print(b) #2
print(others) #[3,4] list
# print(type(others))


# --------- swapping elements --------

a = 1
b = 2
a,b = b,a
print(a)
print(b)


# ------- zipping tuples --------

# a = (1,2,3,4)
# b = (5,6,7,8)

# print(tuple(zip(a,b)))




