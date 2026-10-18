from typing import List

class Node:
	def __init__(self,data:int):
		self.data = data
		self.back = None
		self.next = None


def printLL(head:Node):
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next


def countLL(head:Node) -> int:
	temp = head
	cnt = 0
	while temp:
		temp = temp.next
		cnt += 1
	return cnt


def initializeDLL(arr : List) -> Node:
	if len(arr) == 0:
		return None
	head = Node(arr[0])
	prev = head
	for i in range(1,len(arr)):
		n = Node(arr[i])
		n.back = prev
		prev.next = n
		prev = n
	return head


# ---------------------- Insertion "Before" Head ----------------------

def insertionBeforeHead(head : Node, el : int) -> Node:
	# ll is empty
	if head is None:
		return Node(el)

	newHead = Node(el)
	newHead.next = head
	head.back = newHead
	return newHead

# arr = [1,2,3,4,5]
# initHead = initializeDLL(arr)
# head = insertionBeforeHead(initHead,10)
# printLL(head)

def insertionBeforeTail(head : Node, el: int) -> Node:
	# if ll is empty
	if head is None:
		return Node(el)
	# if we have only one element and that is tail itself
	if head.next is None:
		newHead = Node(el)
		newHead.next = head
		head.back = newHead
		return newHead

	temp = head
	while temp.next is not None:
		temp = temp.next
	newNode = Node(el)
	newNode.next = temp
	temp.back.next = newNode
	newNode.back = temp.back
	temp.back = newNode

	return head

# arr = [1,2,3,4,5]
# initHead = initializeDLL(arr)
# head = insertionBeforeTail(initHead,10)
# printLL(head)

def insertionBeforekthValue(head : Node, el: int, k : int) -> Node:
	length = countLL(head)
	if k > length:
		raise TypeError('Cannot Insert At length Greater Than Lenght of linked list')		
	elif k == 1:
		if head is None:
			return Node(el)
		else:
			# insert before head as empty ll is not possible at 
			newHead = Node(el)
			newHead.next = head
			head.back = newHead
			return newHead
	elif k == length:
		temp = head
		while temp.next is not None:
			temp = temp.next
		newNode = Node(el)
		newNode.next = temp
		newNode.back = temp.back
		temp.back.next = newNode
		temp.back = newNode
		return head
	else:
		temp = head
		cnt = 1
		while cnt != k:
			temp = temp.next
			cnt += 1
		newNode = Node(el)
		newNode.next = temp
		newNode.back = temp.back
		temp.back.next = newNode
		temp.back = newNode
		return head		
	

# arr = [1,2,3,4,5]
# initHead = initializeDLL(arr)
# head = insertionBeforekthValue(initHead,10,5)
# printLL(head)
		

def insertBeforeNode(node : Node, val : int):
	prev = node.back

	# we need to insert before tail and node given is tail node
	newNode = Node(val)
	newNode.back = prev
	prev.next = newNode
	newNode.next = node
	node.back = newNode


arr = [1,2,3,4,5]
initHead = initializeDLL(arr)
temp = initHead
cnt = 1
while temp:
	if cnt == 3:
		break
	temp = temp.next
	cnt += 1
# want to insert 10 before third node
insertBeforeNode(temp, 10)
printLL(initHead)
		







	

	