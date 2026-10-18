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

# def bruteForcecheckPalindrome(head:Node) -> bool:
# 	if head.next is None:
# 		return True 
# 	el = []
# 	temp = head
# 	while temp:
# 		el.append(temp.data)
# 		temp = temp.next
# 	for i in range(len(el)):
# 		if el[i] != el[len(el) - i - 1]:
# 			return False
# 	return True

# res = bruteForcecheckPalindrome(initHead) 	
# print(res)


def optimalSolnCheckPalindrome(head:Node) -> bool:
	if head.next is None:
		return True

	slow = head
	fast = head.next

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	prev = None
	curr = slow.next
	while curr:
		front = curr.next
		curr.next = prev
		prev = curr
		curr = front
	newHead = prev

	while head and newHead:
		if head.data != newHead.data:
			return False
		head = head.next
		newHead = newHead.next
	return True


res = optimalSolnCheckPalindrome(initHead)
print(res)
	

	
	

	


