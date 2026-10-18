nums = [0, 3, 4, 7, 10, 9]
k = 4

res = -1

nums = sorted(nums)

low = 1
# max - min
high = nums[len(nums) - 1] - nums[0]

def canWePlace(arr,dist,target):
	cnt = 1
	last = arr[0]
	for i in range(1,len(arr)):
		if (arr[i] - last) >= dist:
			cnt += 1
			last = arr[i]
	if cnt >= target:
		return True
	else:
		return False



while low <= high:
	mid = (low + high) // 2
	if canWePlace(nums,mid,k):
		res = mid
		low = mid + 1
	else:
		high = mid - 1

print(res)