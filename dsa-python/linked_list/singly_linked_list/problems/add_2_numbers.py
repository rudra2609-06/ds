l1 = [2,4,3]
l2 = [5,6,4]

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



L1 = initializeSLL(l1)
L2 = initializeSLL(l2)



def add2Numbers(h1:Node,h2:Node) -> Node:
	dummyNode = Node(-1)
	curr = dummyNode
	t1 = h1
	t2 = h2
	carry = 0
	# continue when atleast one list have node
	while t1 != None or t2 != None:
		total = carry
		if t1:
			total += t1.data
		if t2:
			total += t2.data
		newNode = Node(total % 10)
		carry = total // 10
		curr.next = newNode
		curr = curr.next

		if t1:
			t1 = t1.next
		if t2:
			t2 = t2.next
	if carry:
		newNode = Node(carry)
		curr.next = newNode
		curr = curr.next
	return dummyNode.next

head = add2Numbers(L1,L2)
printLL(head)





		


	
	
			







