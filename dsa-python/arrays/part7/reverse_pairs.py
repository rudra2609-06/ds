# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].

arr = [2,4,3,5,1]
n = len(arr)

res = 0

# ----------------- Brute Force Approach -----------------

# for i in range(n - 1):
# 	first_element = arr[i]
# 	j = i + 1
# 	while j <= n - 1:
# 		second_element = arr[j]
# 		if first_element > (second_element * 2):
# 			res += 1
# 		j += 1

# print(res)

# ----------------- Optimal Approach -----------------

def merge(arr,n,low,mid,high):
	left = low
	right = mid + 1

	temp_l1 = []

	while left <= mid and right <= high:
		if arr[left] <= arr[right]:
			temp_l1.append(arr[left])
			left += 1
		else:
			temp_l1.append(arr[right])
			right += 1
	

	while right <= high:
		temp_l1.append(arr[right])
		right += 1

	while left <= mid:
		temp_l1.append(arr[left])
		left += 1
	
	for i in range(low,high + 1):
		arr[i] = temp_l1[i - low]


def countPairs(arr,low,mid,high):
	cnt = 0
	right = mid + 1
	for i in range(low,mid+1):
		while right <= high and arr[i] > (arr[right] * 2):
			right += 1
		cnt +=  (right - (mid + 1))

	return cnt		



def mergeSort(arr,n,low,high):
	cnt = 0
	if low >= high:
		return cnt
	mid = (low + high) // 2
	cnt += mergeSort(arr,n,low,mid)
	cnt += mergeSort(arr,n,mid + 1,high)
	cnt += countPairs(arr,low,mid,high)
	merge(arr,n,low,mid,high)
	return cnt



res = mergeSort(arr,n,0,n - 1)
print(res)





