# Book Allocation Problem

nums = [12, 34, 67, 90]	
m = 2
total = sum(nums)


low = max(nums)
high = sum(nums)

res = -1

def student_allocation(arr,cap):
	current = 0
	student = 1

	for pages in arr:
		if current + pages <= cap:
			current += pages
		else:
			student += 1
			current = pages

	return student


while low <= high:

	mid = (low + high) // 2

	if student_allocation(nums,mid) <= m:
		res = mid
		high = mid - 1
	else:
		low = mid + 1

print(res)