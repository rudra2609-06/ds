# itemwise

l = [1,2,3,4]

for val in l:
	print(val)

# indexwise

for i in range(0,len(l)):
	print(l[i])


# zip: zip returns object which we can convert to list. what zip does is that it takes the first items of list indexwise and then pairs it with second item of list indexwise

# add to elements of two list indexwise and put them into third list

l1 = [1,2,3,4]
l2 = [5,6,7,8]


print(list(zip(l1,l2)))

l3 = [i + j for i,j in zip(l1,l2)]
print(l3)


