arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
k = 10


class Solution:
	def minimizeMaxDist(self,arr,k):
		low = min(arr)
		high = max(arr)
		res = -1

		while low <= high:
			mid = (low + high) / 2
			print(mid)
			if self.numberOfGasStations(arr,mid)<= k:
				res = mid
				high = mid - 1
			else:
				low = mid + 1 
		return res

	def numberOfGasStations(self,arr,mid):
		count = 1
		curr = 0

		for dist in arr:
			if curr + dist <= mid:
				curr += dist
			else:
				curr = dist
				count += 1
		return count

s = Solution()
res = s.minimizeMaxDist(arr,k)
print(res)
