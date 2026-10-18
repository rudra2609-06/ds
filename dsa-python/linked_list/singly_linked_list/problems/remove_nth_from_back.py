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


initHead = initializeSLL([1,2])



# def removeNthFromBack(head:Node,n:int) -> Node:
# 	if head is None:
# 		return None
# 	if head.next is None and n == 1:
# 		return None

# 	temp = head
# 	l = 0

# 	while temp:
# 		temp = temp.next
# 		l += 1

# 	temp = head
# 	if l == n:
# 		head = temp
# 		newHead = temp.next
# 		head.next = None
# 		return newHead

# 	targetNode = l - n
# 	cnt = 1
# 	while cnt != targetNode:
# 		temp = temp.next
# 		cnt += 1
# 	node = temp.next
# 	temp.next = temp.next.next
# 	node.next = None
# 	return head


# head = removeNthFromBack(initHead,2)
# printLL(head)


def removeNthFromBackSinglePass(head:Node, n:int) -> Node:
	if head is None:
		return None
	if head.next is None and n == 1:
		return None

	fast = head
	slow = head
	while n != 0:
		fast = fast.next
		n -= 1
	if not fast:
		oldHead = head
		newHead = head.next
		oldHead.next = None
		return newHead
		
	while fast.next is not None:
		fast = fast.next
		slow = slow.next
	old = slow.next
	slow.next = slow.next.next
	old.next = None
	return head

head = removeNthFromBackSinglePass(initHead,2)
printLL(head)
	

