class Node:
	def __init__(self,data):
		self.data = data
		self.prev = None	
		self.next = None


def initializeDLL(l1) -> Node:
	temp = Node(l1[0])
	head = temp
	for i in l1[1:]:
		newNode = Node(i)
		newNode.prev = temp
		temp.next = newNode
		temp = temp.next
	return head

def printLL(head:Node):
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next


l1 = [1,2,3]
initHead = initializeDLL(l1)


def removeDuplicatesFromSortedDLL(head:Node) -> Node:
	if head is None or head.next is None:
		return head

	temp = head
	while temp:
		front = temp.next
		if not front:
			break
		if temp.data == front.data:
			temp.next = front.next
			front.next.prev = temp
		else:
			temp = temp.next

	return head


head = removeDuplicatesFromSortedDLL(initHead)
printLL(head)


		
		