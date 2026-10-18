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



def segregateOddAndEvens(head:Node) -> Node:

	if head is None or head.next is None:
		return head
	
	odd = head
	even = head.next
	evenHead = head.next
	while even and even.next:
		temp = even.next
		odd.next = even.next
		even.next = temp.next
		odd = odd.next
		even = even.next
	odd.next = evenHead
	return head

thead = initializeSLL([1,2,3,4,5,6,7,8])
head = segregateOddAndEvens(thead)
printLL(head)
	






