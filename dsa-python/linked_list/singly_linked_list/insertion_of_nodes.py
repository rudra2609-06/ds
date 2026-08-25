class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

n1 = Node(2)
n2 = Node(3)
n3 = Node(1)
n4 = Node(8)

n1.next = n2
n2.next = n3
n3.next = n4
head = n1

def printLl(head):
	temp = head
	while temp != None:
		print(temp.data)
		temp = temp.next

def calLenOfLL(head):
	temp = head
	cnt = 0
	while temp:
		temp = temp.next
		cnt += 1
	return cnt




# insertion before head

# input ll:- 2,3,1,8
# el:- 5
# output ll:- 5,2,3,1,8


# def insertHead(head,el):
# 	if head == None:
# 		return Node(el)
# 	n0 = Node(el)
# 	n0.next = head
# 	return n0

# head = insertHead(n1,5)
# printLl(head)


# insertion after last/tail element

# def insertAtLast(head,el):
# 	if head == None:
# 		return Node(el)
# 	temp = head
# 	while temp.next != None:
# 		temp  = temp.next
# 	newTail = Node(el)
# 	newTail.next = None
# 	temp.next = newTail
# 	return head

# head = insertAtLast(n1,30)
# printLl(head)



# insertion at kth index

# suppose lenght of ll is n then k will range from 1 -> n + 1 

# input ll:- 2,3,1,8
# here, length is 4 that means k will possibly be 1 which means insert at head case, if 5 means insert at tail case if between that we need to tackle.

# def insertkth(head,el,k):   
# 	# if ll empty 
# 	if head == None:
# 		# if the insertion index is head we can insert a default node
# 		if k == 1:
# 			return Node(el)
# 		# if ll is empty and kth idx is other than head not possible to insert
# 		else:
# 			return None
# 	# if k is 1 
# 	if k == 1:
# 		newHead = Node(el)
# 		newHead.next = head
# 		return newHead
# 	# new tail needs to be inserted as k = len + 1
# 	elif k > calLenOfLL(head):
# 		temp = head
# 		while temp.next != None:
# 			temp = temp.next
# 		newTail = Node(el)
# 		newTail.next = None
# 		temp.next = newTail
# 		return head
# 	# in range of 2 and len of ll
# 	else:
# 		temp = head
# 		cnt = 1
# 		while cnt != k - 1:
# 			temp = temp.next
# 			cnt += 1
# 		newNode = Node(el)
# 		newNode.next = temp.next
# 		temp.next = newNode
# 		return head


# head = insertkth(n1,4,1)  # -> this will give 4,2,3,1,8 if case will run
# head = insertkth(n1,4,5)  # -> this will give 2,3,1,8,4 elif case will run
# head = insertkth(n1,4,3)  # -> this will give 2,3,4,1,8 else case will run
# printLl(head) 

# insertion value before particular value and it is guaranted that value before which it should be inserted is present


# input ll:- 2,3,1,8
# x = 3
# el = 10
# output :- 2,10,3,1,8


def insertBeforeValue(head,val,x):
	# only one element present and that is the ele before which we will be inserting
	if head.data == x:
		temp  = head
		n0 = Node(val)
		n0.next = temp
		return n0
	else:
		temp = head
		prev = None
		while temp:
			if temp.data == x:
				new = Node(val)
				new.next = prev.next
				prev.next = new	
				break


			prev = temp
			temp = temp.next
		return head


head = insertBeforeValue(n1,90,2)
head = insertBeforeValue(n1,90,1)   
printLl(head)



