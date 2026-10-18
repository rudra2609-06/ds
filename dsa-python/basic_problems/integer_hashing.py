l1 = [1,1,2,5,3,5]

l1_hash = [0] * (max(l1) + 1)

for i in range(len(l1)):
	l1_hash[l1[i]] += 1


for i in l1_hash:
	print(i)

print("occurence of 1: ",l1_hash[1])

