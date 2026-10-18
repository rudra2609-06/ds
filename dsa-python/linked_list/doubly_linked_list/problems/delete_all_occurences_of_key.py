class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

def initializeDLL(l1):
	temp = Node(l1[0])
	head = temp
	for i in l1[1:]:
		newNode = Node(i)
		temp.next = newNode
		newNode.prev = temp
		temp = temp.next
	return head

def printLL(head:Node):
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next



initHead = initializeDLL([7,7,7,7])



def deleteAllOccurences(head:Node, target: int) -> Node:
	if head is None:
		return None
	if head.next is None and head.data == target:
		return None
	temp = head
	while temp:
		front = temp.next
		prev = temp.prev
		if temp.data == target:
			if front:
				front.prev = prev
			if prev:
				prev.next = front
			else:
				head = front
		else:
			front = temp.next
			prev = front
		temp = front					
	return head

head = deleteAllOccurences(initHead,7)
printLL(head)
	





