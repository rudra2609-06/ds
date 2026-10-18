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



initHead = initializeSLL([1,2,3,4,5])

def reverseSLL(head:Node) -> Node:
	prev = None
	curr = head
	while curr:
		front = curr.next
		curr.next = prev
		prev = curr
		curr = front
	return prev 	

head = reverseSLL(initHead)
printLL(head)