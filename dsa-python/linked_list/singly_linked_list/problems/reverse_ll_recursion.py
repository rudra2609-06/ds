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

l1 = [1,2,3,4,5]
initHead = initializeSLL(l1)


def reverseLL(head:Node) -> Node:
	if head is None or head.next is None:
		return head
	newHead = reverseLL(head.next)
	front = head.next
	front.next = head
	head.next = None
	return newHead

head = reverseLL(initHead)
printLL(head)