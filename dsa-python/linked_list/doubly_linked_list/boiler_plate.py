class Node:
	def __init__(self,data):
		self.data = data
		self.back = None
		self.next = None


# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)

# n1.next = n2
# n2.back = n1
# n2.next = n3
# n3.back = n2
# n3.next = n4
# n4.back = n3
# n4.next = n5
# n5.back = n4

# -------- Through loop ---------

arr  = [1,2,3,4,5]

head = Node(arr[0])
prev = head

for i in range(1,len(arr)):
	temp = Node(arr[i])
	temp.back = prev
	prev.next = temp
	prev = temp

temp1 = head
while temp1:
	print(temp1.data)
	temp1 = temp1.next

		