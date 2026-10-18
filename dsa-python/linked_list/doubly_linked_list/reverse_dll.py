from typing import List

class Node:
	def __init__(self,data):
		self.data = data
		self.back = None
		self.next = None


class Stack:
	def __init__(self):
		self.top = None
		

	def push(self,data):
		newNode = Node(data)
		newNode.next = self.top
		if self.top is not None:
			self.top.back = newNode
		self.top = newNode

	def pop(self):
		if self.isEmpty():
			raise IndexError('Stack is empty')
		elToPop = self.top
		self.top = self.top.next
		if self.top is not None:
			self.top.back = None
		elToPop.next = None
		return elToPop.data

	def peek(self):
		return self.top.data if self.top is not None else None

	def isEmpty(self):
		return self.top is None	



def initializeDll(arr : List) -> Node:
	head = Node(arr[0])
	prev = head
	for i in range(1,len(arr)):
		newNode = Node(arr[i])
		prev.next = newNode
		newNode.back = prev
		prev = newNode
	return head

def printLL(head:Node):
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next


arr = [1,2,3,4,5]
initHead = initializeDll(arr)

# ---------- brute force soln to reverse the dll elements using stack ---------

# def bruteForce(head:Node, s : Stack) -> Node:
# 	temp = head
# 	while temp:
# 		s.push(temp.data)
# 		temp = temp.next

# 	temp = head
# 	while temp:
# 		temp.data = s.pop()
# 		temp = temp.next

# 	return head

# s = Stack()
# head = bruteForce(initHead,s)
# printLL(head)


# TC : O(2N)
# SC : O(N)

# ------------ Optimal (Single Pass) Soln to reverse the dll elements ---------

def swapping(head : Node) -> Node:
	if head is None or head.next is None:
		return head
	curr = head
	last = None
	while curr is not None:
		last = curr.back
		curr.back = curr.next
		curr.next = last
		curr = curr.back
	return last.back


head = swapping(initHead)
printLL(head)

# TC : O(N)
# SC : O(1)