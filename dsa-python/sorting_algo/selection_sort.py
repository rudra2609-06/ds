l1 = [13,46,52,20,9]

for i in range(len(l1)):
	min_idx = i
	for j in range(i + 1,len(l1)):
		if l1[j] < l1[min_idx]:
			min_idx = j
	
	l1[i],l1[min_idx] = l1[min_idx],l1[i]


print(l1)