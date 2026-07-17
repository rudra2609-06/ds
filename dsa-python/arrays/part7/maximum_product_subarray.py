# you are given an array you need to return sub-array whose product is tend to be maximum from all other subarray's product

arr = [2,3,-2,4]

# def maximum_product_subarray(ar):
# 	res = -1

# 	for i in range(len(ar)):
# 		product = ar[i]
# 		j = i + 1
# 		while j <= (len(ar) - 1):
# 			product *= ar[j]
# 			res = max(product,res)
# 			j += 1
		
# 	return res

# res = maximum_product_subarray(arr)
# print(res)


def maximum_product_subarray(ar):
	leftToRight = 1
	RightToLeft = 1
	n = len(ar)
	maxProd = float('-inf')
	for i in range(n):
		if leftToRight == 0:
			leftToRight = 1
		else:
			RightToLeft = 1
		
		leftToRight *= ar[i]

		j = n - i - 1
		RightToLeft *= ar[j]

		maxProd = max(leftToRight,RightToLeft,maxProd)
	return maxProd



res = maximum_product_subarray(arr)
print(res)