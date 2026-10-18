# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


bloomDay = [1,10,3,10,2]
m = 3
k = 1



# -------------- Brute Force Approach --------------

# if m * k > len(bloomDay) return -1 --> edge case

days_to_wait = -1
for i in range(1,max(bloomDay)):
	streak = 0
	bouquets = 0
	for j in range(len(bloomDay)):
		if i <= bloomDay[j]:
			streak += 1
			if streak == k:
				bouquets += 1
				streak = 0
		else:
			streak = 0
	if bouquets == m:
		days_to_wait = i
		break
		

print(days_to_wait)


low = 1
high = max(bloomDay)

# -------------- Optimal Approach --------------

# if (m * k) > len(arr) then return with -1 not possible

while low <= high:
	mid = (low + high) // 2
	streak = 0
	bouquets = 0
	for i in range(len(bloomDay)):
		if bloomDay[i] <= mid:
			streak += 1
			if streak == k:
				bouquets += 1
				streak = 0
		else:
			streak = 0

	if bouquets < m:
		low = mid + 1
	else:
		days_to_wait = mid
		high = mid - 1



# print(days_to_wait)

		 
