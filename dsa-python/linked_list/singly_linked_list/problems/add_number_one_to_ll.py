# given a ll consider it as number: head -> 1 -> 2 -> 3
# read it as, 123 
# now you need to add one to this number and return it
# that is 124

# Eg: head->9->9
# 1 -> 0 -> 0

# Here, the given constraint is such that the provided Nodes will have value in range of 0 to 9 no leading 0 other than the 0 value it self

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

l1 = [1,2,9]
initHead = initializeSLL(l1)


# ------- 1st optimal soln --------

def reverseLL(head:Node) -> Node:
	curr = head
	prev = None
	while curr:
		front = curr.next
		curr.next = prev
		prev = curr
		curr = front
	return prev


# def add1ToLL(head:Node) -> Node:
	
# 	if head is None:
# 		return None
# 	revHead = reverseLL(head)
# 	temp = revHead
# 	carry = 1
# 	while temp:
# 		temp.data = temp.data + carry
# 		if temp.data > 9:
# 			temp.data = 0
# 			carry = 1
# 		else:
# 			break
# 		temp = temp.next
# 	head = reverseLL(revHead)
# 	if carry:
# 		newHead = Node(1)
# 		newHead.next = head
# 		return newHead
# 	return head



# res = add1ToLL(initHead)
# printLL(res)


# ------- 2nd optimal soln --------


def addOneUntil(head:Node) -> Node:
	if head is None:
		return 1

	carry = addOneUntil(head.next)
	total = head.data + carry
	head.data = total % 10
	return total // 10

def addOne(head:Node) -> Node:
	carry = addOneUntil(head)
	if carry:
		newHead = Node(carry)
		newHead.next = head
		head = newHead
	return head

head = addOne(initHead)
printLL(head)