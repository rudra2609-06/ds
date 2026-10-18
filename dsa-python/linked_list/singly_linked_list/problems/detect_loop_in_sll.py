from typing import List
# here just the soln is written first in code form first is brute force and optimal one by one

# class BruteForceSoln:
#     # function to detect loop in linked list
#     def detectLoop(self, head):
#         # Initialize a pointer 'temp'
#         # at the head of the linked list
#         temp = head

#         # Create a set to keep track of
#         # encountered nodes
#         nodeMap = {}

#         # Step 2: Traverse the linked list
#         while temp is not None:
#             # If the node is already in the
#             # map, there is a loop
#             if temp in nodeMap:
#                 return True
#             # Store the current node
#             # in the map
#             nodeMap[temp] = 1

#             # Move to the next node
#             temp = temp.next

#         # Step 3: If the list is successfully traversed 
#         # without a loop, return false
#         return False


# class OptimalSoln:
#     # Function to detect a loop in a linked
#     # list using the Tortoise and Hare Algorithm
#     def hasCycle(self, head):
#         # Initialize two pointers, slow and fast,
#         # to the head of the linked list
#         slow = head
#         fast = head

#         # Step 2: Traverse the linked list with
#         # the slow and fast pointers
#         while fast is not None and fast.next is not None:
#             # Move slow one step
#             slow = slow.next
#             # Move fast two steps
#             fast = fast.next.next

#             # Check if slow and fast pointers meet
#             if slow == fast:
#                 return True  # Loop detected

#         # If fast reaches the end of the list,
#         # there is no loop
#         return False


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

head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3  


# ------ Optimal Soln ------


def detectLoopInLL(head:Node) -> bool:
	if head is None:
		return False
	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False

res = detectLoopInLL(head)
print(res)
	