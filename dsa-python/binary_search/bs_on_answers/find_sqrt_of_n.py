n = 28

# --------------- Brute Force Approach ---------------

res = 1

for num in range(n // 2):
	prod = num * num
	if prod == n:
		res = num
		break
	elif prod > n:
		res = num - 1
		break

# --------------- Optimal Approach ---------------

low = 0
high = n 

res = 1

while low <= high:
	mid = (low + high) // 2
	prod = mid * mid

	if prod <= n:
		res = prod
		low = mid + 1
	else:
		high = mid - 1


print(res)
