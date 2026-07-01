# LeetCode Notes:
# Problem: Merge overlapping intervals and return the minimum number of merged intervals.
# Idea: Sort by start time, then keep extending the current interval while overlap continues.
# Trick: If next start <= current end, both intervals belong to the same merged block.
# Dry run: (1,3) + (2,6) -> (1,6), and (15,18) + (16,17) stays (15,18).
# TC and SC: O(N log N) time because sorting dominates, O(1) extra space apart from the answer list.

intervals = [
	(1,3),
	(2,6),
	(8,9),
	(9,11),
	(8,10),
	(2,4),
	(15,18),
	(16,17)
]

minimum_possible_overlapping_intervals = []

intervals.sort()

# ---------------- Brute Force Solution ---------------

# for i in range(len(intervals)):

# 	start = intervals[i][0]
# 	end = intervals[i][1]
# 	if len(minimum_possible_overlapping_intervals) > 0 and end <= 		   minimum_possible_overlapping_intervals[-1][1]:
# 		continue	
	
# 	for j in range(i+1,len(intervals)):
# 		if intervals[j][0] <= end:
# 			end = max(end,intervals[j][1])
# 		else:
# 			break
# 	minimum_possible_overlapping_intervals.append([start,end])

# print(minimum_possible_overlapping_intervals)

# TC : O(NlogN) + O(N2) worst case
# SC : O(1)

# ---------------- Optimal Solution ---------------

# start = intervals[0][0]
# end = intervals[0][1]

# for i in range(1,len(intervals)):
# 	if intervals[i][0] <= end:
# 		end = max(end,intervals[i][1])
# 	else:
# 		minimum_possible_overlapping_intervals.append([start,end])
# 		start = intervals[i][0]
# 		end  = intervals[i][1]
# minimum_possible_overlapping_intervals.append([start,end])

# print(minimum_possible_overlapping_intervals)

# TC : O(Nlogn) + O(N)
# SC : O(1)
