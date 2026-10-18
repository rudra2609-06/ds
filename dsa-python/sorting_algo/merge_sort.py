l1 = [3,1,2,4,1,5,2,6,4]

def merge(l1,low,mid,high):

	leftPointer = low
	righPointer = mid + 1
	temp_l1 = []

	while leftPointer <= mid and righPointer <= high:
		if l1[leftPointer] <= l1[righPointer]:
			temp_l1.append(l1[leftPointer])
			leftPointer += 1
		else:
			temp_l1.append(l1[righPointer])
			righPointer += 1
	
	while righPointer <= high:
		temp_l1.append(l1[righPointer])
		righPointer += 1

	while leftPointer <= mid:
		temp_l1.append(l1[leftPointer])
		leftPointer += 1

	
	for i in range(low,high + 1):
		l1[i] = temp_l1[i - low]

def divideList(l1,low,high):
	if low >= high:
		return
	
	mid = (low + high) // 2

	divideList(l1,low,mid)
	divideList(l1,mid + 1,high)

	merge(l1,low,mid,high)


divideList(l1,0,len(l1) - 1)
print(l1)


