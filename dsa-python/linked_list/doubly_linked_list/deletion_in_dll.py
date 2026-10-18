class Node:
	def __init__(self,data):
		self.data = data
		self.back = None
		self.next = None


def printLL(head):
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next

def countLL(head) -> int:
	temp = head
	cnt = 0
	while temp:
		temp = temp.next
		cnt += 1
	return cnt

def initializeDLL(arr):
	if len(arr) == 0:
		return None
	head = Node(arr[0])
	prev = head
	for i in range(1,len(arr)):
		temp = Node(arr[i])
		temp.back = prev
		prev.next = temp
		prev = temp
	return head


# ---------------------- Deletion of Head ----------------------

def deletionOfHead(head):
	# dll is empty or only one Node in dll
	if head == None or head.next == None:
		return None
	# more than one nodes
	temp = head
	newHead = temp.next
	newHead.prev = None
	del temp
	return newHead

# arr = [1,2,3,4,5]
# head = deletionOfHead(initializeDLL(arr))
# printLL(head)


# ----------------------  Deletion of Tail ----------------------

# def deletionOfTail(head):
# 	# if ll is empty or only one element in it
# 	if head == None or head.next == None:
# 		return None
# 	temp = head
# 	while temp.next.next != None:
# 		temp = temp.next
# 	newTail = temp
# 	newTail.next = None
# 	return head

# arr = [1,2,3,4,5]
# head = deletionOfTail(initializeDLL(arr))
# printLL(head)

# ---------------------- Deletion The kth element ----------------------
# in this problem it is guaranteed to have atleast one node and k will range from 1 to length of linked list

# def deletekthElement(head,k,n):
# 	# to delete first node
# 	if k == 1:
# 		# if only one node in dll
# 		if head.next == None:
# 			return None
# 		# more than one node in dll but to delete the first node
# 		else:
# 			temp = head
# 			newHead = temp.next
# 			newHead.back = None
# 			return newHead
# 	# to delete tail element as k == N
# 	elif k == n:
# 		temp = head
# 		while temp.next != None:
# 			temp = temp.next
# 		newTail = temp.back
# 		newTail.next = None
# 		return head
# 	# k b/w 1 and N
# 	else:
# 		temp = head
# 		cnt = 1
# 		while cnt != k:
# 			temp = temp.next
# 			cnt += 1
# 		prevElement = temp.back
# 		prevElement.next = temp.next
# 		return head

# arr = [1,2,3,4,5]
# initialHead = initializeDLL(arr)
# head = deletekthElement(initialHead,1,countLL(initialHead))
# printLL(head)


# ---------------------- Deletion Of Particular Node ----------------------
# in this case Node provided to you is not the head other than head
# that means ll has more than one element

def deleteParticularNode(node):
	
	prev = node.back
	front = node.next

	if front == None:
		prev.next = None
	else:
		front.back = prev
		prev.next = front	

arr = [1,2,3,4,5]
head = initializeDLL(arr)
deleteParticularNode(head.next)
printLL(head)

	










	


		

	

