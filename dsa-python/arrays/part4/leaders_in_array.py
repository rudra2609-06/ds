l1 = [10,22,12,3,0,6]

# leaders_of_l1 = []

# leaders_of_l1.append(l1[len(l1) - 1])

# for i in range(len(l1) - 1):
# 	leader_assumed = l1[i]
# 	isLeader = True
# 	for j in range(i+1,len(l1)):
# 		if l1[j] > leader_assumed:
# 			isLeader = False
# 			break9+-    
# 	if isLeader:
# 		leaders_of_l1.append(leader_assumed)

# print(leaders_of_l1)


# TC : O(N2)
# SC : O(N) (not for solving problem but for storing the result) (if arr in non-ascending order every one is leader worst case senario)

# ---------- Optimal Solution ------------

# leaders_of_l1 = []

# leaders_of_l1.append(l1[len(l1) - 1])

# leader_so_far = l1[len(l1) - 1]


# for i in range(len(l1) - 2,-1,-1):
# 	if l1[i] > leader_so_far:
# 		leaders_of_l1.append(l1[i])
# 		leader_so_far = leaders_of_l1[-1]


# print(leaders_of_l1)

# TC : O(N)
# SC : O(1) for solving problem and O(N) for storing result




			

	





