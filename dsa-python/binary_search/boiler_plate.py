arr = [3,4,5,9,12,20,22]

n = len(arr)

target = 9

# ----------- iterative way -------------

# def searchTarget(arr,n,target):
#     low = 0
#     high = n - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         # if mid element is greater eliminate right search space by bringing right at mid - 1
#         elif arr[mid] > target:
#             high = mid - 1
#         # if mid element is lesser eliminate left search space by bringing left at mid + 1
#         else:
#             low = mid + 1
#     return -1

# res = searchTarget(arr,n,target)
# print(res)


# ----------- recursive way -------------



def splitAndSearch(arr,n,target,low,high):
	if low > high:
		return -1
	mid = (low + high) // 2
	if arr[mid] == target:
		return mid
	elif arr[mid] > target:
		high = mid - 1
		return splitAndSearch(arr,len(arr),target,low,high)
	else:
		low = mid + 1
		return splitAndSearch(arr,len(arr),target,low,high)
	
res = splitAndSearch(arr,n,target,0,n-1)
print(res)

