m = 16
n = 2

# --------------- Brute Force Approach ---------------

# res = -1


# for i in range(m + 1):
# 	power_prod = 1
# 	for j in range(n):
# 		power_prod *= i

# 	if power_prod == m:
# 		res = i

# print(res)


# --------------- Optimal Approach ---------------

res = -1

low = 0
high = m // 2

# if mid power n is greater then m -> 2
# if mid power n is smaller then m -> 0
# if mid power n is equal to m -> 1

def calPowerProd(m,mid,n):
	temp = 1
	for _ in range(n):
		temp *= mid
		if temp > m:
			return 2
		if temp == m:
			return 1
	return 0

while low <= high:
	mid = (low + high) // 2

	power_prod = calPowerProd(m,mid,n)

	if power_prod == 1:
		res = mid
		break
	elif power_prod == 0:
		low = mid + 1
	else:
		high = mid - 1

print(res)


