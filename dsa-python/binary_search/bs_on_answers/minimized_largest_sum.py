nums = [7,2,5,10,8]
k = 2
n = len(nums)


class Solution:
	def splitArr(self,nums,k):
		low = max(nums)
		high = sum(nums)
		res = -1
		while low <= high:
			mid = (low + high) // 2

			if self.numberOfArr(nums,mid) <= k:
				res = mid
				high = mid - 1
			else:
				low = mid + 1
		return res

	def numberOfArr(self,nums,mid):
		count = 1
		curr = 0

		for element in nums:
			if curr + element <= mid:
				curr += element
			else:
				count += 1
				curr = element
		return count

s = Solution()
res = s.splitArr(nums,k)
print(res)
