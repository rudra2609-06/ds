class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = None

head = node1
element = 4


# temp = head
# isPresent = False
# while temp:
# 	if temp.data == element:
# 		isPresent = True
# 		break
# 	temp = temp.next

# if isPresent:
# 	print('Yes')
# else:
# 	print('No')

	

curr = head
while curr:
	print(curr.data)
	curr = curr.next

# ------ OR ------

# currN = head
# while True:
# 	print(currN.data)
# 	currN = currN.next
# 	if currN == None:
# 		break









