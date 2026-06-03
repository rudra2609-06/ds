# similar to list

# + and *
t1 = (1,2,3,4)
t2 = (4,5,6,7)

print(t1 + t2)

print(t1 * 3)

# membership in and not in

print(2 in t1)
print(2 not in t1)

#iteration

for i in t1: 
	print(i)


# ------- NOTE ------------

a = [1,2,3]
b = a

a = a + (4,)
print(a) #(1,2,3,4)
print(b) #(1,2,3)