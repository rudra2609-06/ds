from typing import List


# Given the head of a sorted doubly linked list of positive distinct integers, and a target integer, return a 2D array containing all unique pairs of nodes (a, b) such that a + b == target.

# Each pair should be returned as a 2-element array [a, b] with a < b. The list is sorted in ascending order. If there are no such pairs, return an empty list.

class Node:
	def __init__(self,data):
		self.data = data
		self.prev = None	
		self.next = None


def initializeDLL(l1) -> Node:
	temp = Node(l1[0])
	head = temp
	for i in l1[1:]:
		newNode = Node(i)
		newNode.prev = temp
		temp.next = newNode
		temp = temp.next
	return head

def printLL(head:Node):
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next

initHead = initializeDLL([2, 3, 5, 9])

def findPairs(head:Node,target:int) -> list:
	if head is None or head.next is None:
		return list()
	nodeMap = {}
	temp = head
	res = []
	while temp:
		diff = target - temp.data
		if diff < 0:
			break
		elif diff in nodeMap:
			smallerVal = diff
			biggerVal = temp.data
			res.append([smallerVal,biggerVal])
		else:
			nodeMap[temp.data] = temp
		temp = temp.next
	return res

res = findPairs(initHead,12)
print(res)




