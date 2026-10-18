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


initHead = initializeSLL([2,1])


def removeMiddleNode2Pass(head:Node) -> Node:
	if head is None or head.next is None:
		return None 
	temp = head
	l = 0
	while temp:
		temp = temp.next
		l += 1
	temp = head
	targetNode = l // 2
	cnt = 0
	while cnt != (targetNode - 1):
		temp = temp.next
		cnt += 1
	oldNode = temp.next
	temp.next = temp.next.next
	oldNode.next = None
	return head


# head = removeMiddleNode2Pass(initHead)
# printLL(head)


def removeMiddleNodeSinglePass(head:Node) -> Node:
	if head is None or head.next is None:
		return None
	prev = None
	slow = head
	fast = head
	while fast and fast.next:
		prev = slow
		slow = slow.next
		fast = fast.next.next
	prev.next = slow.next
	return head

head = removeMiddleNodeSinglePass(initHead)
printLL(head)









