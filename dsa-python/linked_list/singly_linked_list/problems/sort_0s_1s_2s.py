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


ll = [1, 0, 2, 0 , 1]

initHead = initializeSLL(ll)

def sort0s1s2s(head:Node) -> Node:
	if head is None or head.next is None:
		return head

	dummyZero = Node(-1)
	dummyOne = Node(-1)
	dummyTwo = Node(-1)

	zero = dummyZero
	one = dummyOne
	two = dummyTwo

	curr = head

	while curr:
		nextNode = curr.next
		if curr.data == 0:
			zero.next = curr
			zero = zero.next
		elif curr.data == 1:
			one.next = curr
			one = one.next
		else:
			two.next = curr
			two = two.next
		curr = nextNode

	zero.next = dummyOne.next if dummyOne.next else dummyTwo.next
	one.next = dummyTwo.next
	two.next = None
	head = dummyZero.next
	return head


head = sort0s1s2s(initHead)
printLL(head)
	 
