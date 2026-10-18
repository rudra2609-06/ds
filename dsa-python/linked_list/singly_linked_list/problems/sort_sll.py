class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

def initializeSLL(arr) -> Node:
	head = Node(arr[0])
	temp = head
	for i in range(1,len(arr)):
		newNode = Node(arr[i])
		temp.next = newNode
		temp = temp.next
	return head


def printLL(head:Node) -> None:
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next

l1 = [2,5,1,3,-1,0]

initHead = initializeSLL(l1)

def findMid(head:Node) -> Node:
	slow = head
	fast = head.next
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow

def mergeTwoSortedLL(h1:Node,h2:Node) -> Node:
	dummyNode = Node(-1)
	d = dummyNode
	while h1 and h2:
		if h1.data <= h2.data:
			d.next = h1
			h1 = h1.next
		else:
			d.next = h2
			h2 = h2.next
		d = d.next
	if h1:
		d.next = h1
	else:
		d.next = h2
	return dummyNode.next

def sortLL(head:Node) -> Node:
	if head is None or head.next is None:
		return head

	leftmid = findMid(head)
	right = leftmid.next
	leftmid.next = None
	left = head	
	left = sortLL(left)
	right = sortLL(right)
	return mergeTwoSortedLL(left,right)

head = sortLL(initHead)
printLL(head)