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


l1 = [2,4,8,10]
l2 = [1,3,3,6,11,14]

initHead1 = initializeSLL(l1)
initHead2 = initializeSLL(l2)


def mergeTwoSortedLL(h1:Node,h2:Node) -> Node:
	t1 = h1
	t2 = h2
	dummyNode = Node(-1)
	d = dummyNode
	while t1 and t2:
		if t1.data <= t2.data:
			d.next = t1
			d = t1
			t1 = t1.next
		else:
			d.next = t2
			d = t2
			t2 = t2.next
	while t1:
		d.next = t1
		d = t1
		t1 = t1.next

	while t2:
		d.next = t2
		d = t2
		t2 = t2.next
	return dummyNode.next

head = mergeTwoSortedLL(initHead1,initHead2)
printLL(head)
			
