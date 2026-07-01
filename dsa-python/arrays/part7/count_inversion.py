# given an array you need to return total number or pairs such that its left element should be greater than its right element and i (left_pointer) < j (right_pointer)


arr = [5,3,2,4,1]

# ------------- Brute Force Approach -------------

# i = 0
# j = len(arr) - 1

# for i in range(len(arr)):
# 	left_element = arr[i]
# 	j = len(arr)  - 1
# 	while i < j:
# 		if left_element > arr[j]:
# 			res.append([left_element,arr[j]])
# 		# ultimately decrease j
# 		j -= 1

# print(res)

# TC : O(N2)
# SC : O(1)

# ------------- Optimal Approach -------------

def countInversion(arr1,low,mid,high):
	count = 0
	left = low
	right = mid + 1
	res = []
	while left <= mid and right <= high:
		if arr1[left] <= arr1[right]:
			res.append(arr1[left])
			left += 1
		# right is smaller
		else:
			res.append(arr1[right])
			count += (mid - left + 1)
			right += 1

	while left <= mid:
		res.append(arr1[left])
		left += 1
	while right <= high:
		res.append(arr1[right])
		right += 1	
	
	# making actual (in-place) changes
	for i in range(low,high + 1):
		arr[i] = res[i - low]
	return count



def divide(arr1,low,high):
	cnt = 0
	if low >= high:
		return cnt
	mid = (low + high) // 2

	cnt += divide(arr1,low,mid)
	cnt += divide(arr1,mid + 1,high)

	cnt += countInversion(arr1,low,mid,high)
	return cnt
 
res = divide(arr,0,len(arr) - 1)
print(res)

# time complexity :- 0(n log n)
# space complexity:- 0(N)