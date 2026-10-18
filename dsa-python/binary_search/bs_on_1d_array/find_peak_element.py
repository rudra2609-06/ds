nums = [1,2,3,1]

n = len(nums)

peak = -1


def findPeak(arr,n):
	if n == 1:
		return 0

	if arr[1] < arr[0]:
		return 0

	if arr[n - 1] > arr[n - 2]:
		return n - 1

	low = 1
	high = n - 2

	while low <= high:
		mid = (low + high) // 2

		if (arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
			return mid

		elif (arr[mid] > arr[mid - 1]):
			# on increasing curve
			low = mid + 1
		elif (arr[mid] > arr[mid + 1]):
			# on decreasing curve
			high = mid - 1
		else:
			# choose any one side
			low = mid - 1

	return -1









