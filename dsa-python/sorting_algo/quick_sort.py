
def partition(l1,low,high):
	leftPointer = low
	rightPointer = high - 1
	pivot_idx = high

	while leftPointer <= rightPointer:
		while leftPointer <= high and l1[leftPointer] < l1[pivot_idx]:
			leftPointer += 1

		while rightPointer >= leftPointer and l1[rightPointer] >= l1[pivot_idx]:
			rightPointer -= 1
		
		if leftPointer < rightPointer:
			l1[leftPointer],l1[rightPointer] = l1[rightPointer],l1[leftPointer]
		else:
			l1[leftPointer],l1[pivot_idx] = l1[pivot_idx],l1[leftPointer]
	return leftPointer


def divide(l1,low,high):
	
	if low >= high:
		return
	
	pi = partition(l1,low,high)

	# we are not including pi because it is already sorted after getting returned
	divide(l1,low,pi - 1)
	divide(l1,pi + 1,high)


l1 = [3,1,2,4,1,5,2,6,4]
divide(l1,0,len(l1) - 1)
print(l1)


# time complexity : average case : n logn ,worst case : O(n2)
# space complexity : best case : log n , worst case : O(n)
