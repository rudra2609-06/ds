class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
head = n1

def printLl(head):
	temp = head
	while temp != None:
		print(temp.data)
		temp = temp.next
		

# Deletion of head node and returning new head that is very next element

# def deleteHead(head):

# 	# linked list is empty
# 	if head == None:
# 		return head
# 	temp = head
# 	head = head.next
# 	del temp
# 	return head

# head = deleteHead(head=head)

# # cross check new head is changed
# printLl(head)




# Deletion of last element in the linkedlist

# def deleteLastElement(head):
# 	temp = head
# 	# if temp.next == None which means ll has only one element that is last or 
# 	# temp = None ll is empty itself
# 	if temp.next == None or temp == None:
# 		return None

# 	# now it will have min of 2 elements

# 	# stop the loop at last second element
# 	while temp.next.next != None:
# 		temp = temp.next

# 	del temp.next
# 	temp.next = None
# 	return head

# deleteLastElement(head)
# printLl(head)




# Deletion of kth element if exists

# def deleteKthElement(head,k):
# 	if head == None:
# 		return None
# 	if k == 1:
# 		temp = head
# 		head = temp.next
# 		del temp
# 		return head
	
# 	lnCtn = 0
# 	temp =  head
# 	while temp != None:
# 		lnCtn += 1
# 		temp = temp.next

# 	if lnCtn < k:
# 		return None

# 	temp1 = head
# 	cnt = 1
# 	while cnt + 1 != k:
# 		cnt += 1
# 		temp1 = temp1.next
# 	toDelete = temp1.next
# 	temp1.next = temp1.next.next
# 	del toDelete

# 	return head


# head = deleteKthElement(head,1)
# printLl(head)


# Deletion of first element equals to value


# def deteteEl(head,val):
# 	# always check this case
# 	if head == None:
# 		return head
# 	# if the val itself is the head then delete head
# 	if head.data == val:
# 		temp = head
# 		head = temp.next
# 		del temp
# 		return head
# 	temp = head
# 	prev = None
# 	while temp:
# 		if temp.data == val:
# 			prev.next = prev.next.next
# 			del temp.next
# 			break
			
# 		prev = temp
# 		temp = temp.next
# 	return head


	





	





