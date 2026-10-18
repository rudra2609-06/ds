# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours


piles = [3,6,7,11]
h = 8

res = -1

# -------------- Brute Force Approach --------------

# for k in range(1,max(piles) + 1):
# 	time_taken = 0
# 	for p in piles:
# 		time_taken += (p + k - 1) // k
# 	if time_taken <= h:
# 		res = k
# 		break

# print(res)

# -------------- Optimal Approach --------------

# low = 1
# high = max(piles)

# while low <= high:
# 	mid = (low + high) // 2

# 	# calculate how much time taken
# 	time_taken = 0
# 	for p in piles:
# 		time_taken += (p + mid - 1) // mid

# 	if time_taken <= h:
# 		res = mid
# 		high = mid - 1
# 	else:
# 		# increasing speed
# 		low = mid + 1


# print(res)
