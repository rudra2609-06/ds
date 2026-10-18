l1 = [13,46,52,20,9]

for i in range(len(l1)):
	is_swap = False
	for j in range(0,len(l1) - i - 1):
		if l1[j] > l1[j + 1]:
			is_swap = True
			l1[j],l1[j + 1] = l1[j + 1],l1[j]
	if not is_swap:
		break

print(l1)

			

