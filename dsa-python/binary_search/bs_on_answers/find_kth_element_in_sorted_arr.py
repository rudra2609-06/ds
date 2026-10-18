from typing import List

arr1 = [1,3,4,7,10,12]
arr2 = [2,3,6,15]


class Solution:
	def kth(self,arr1 : List[int],arr2 : List[int],k : int) -> int:
		n1 = len(arr1)
		n2 = len(arr2)

		# we want first arr as shorter
		if n1 > n2:
			arr1,arr2 = arr2,arr1
			n1,n2 = n2,n1

		low = max(0,k - n2)
		high = min(k,n1)
		left = k
		res = -1
		while low <= high:
			# number of elements picked from shorter array
			mid1 = (low + high) // 2

			# remaining number of elements picked from longer array to fullfill left half
			mid2 = left - mid1

			l1 = l2 = float('-inf')
			r1 = r2 = float('inf')

			# assigning r1,r2
			if mid1 < n1:
				r1 = arr1[mid1]
			if mid2 < n2:
				r2 = arr2[mid2]

			# assigning l1,l2
			if (mid1 - 1) >= 0:
				l1 = arr1[mid1 - 1]
			if (mid2 - 1) >= 0:
				l2 = arr2[mid2 - 1]

			if (l1 <= r2) and (l2 <= r1):
				res = max(l1,l2)
				break
			elif l1 > r2:
				high = mid1 - 1
			else:
				low = mid1 + 1
		return res


s = Solution()
res = s.kth(arr1,arr2,5)
print(res)

# TC : O(log(min(n1,n2)))
# SC : O(1)

			





