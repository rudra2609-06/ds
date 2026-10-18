from typing import List


class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


def createTestSet(l1: List, l2: List, intersectionVal: int) -> Node:
	common = Node(intersectionVal)
	common.next = Node(9)
	common.next.next = Node(10)

	h1 = Node(l1[0])
	h2 = Node(l2[0])
	temp = h1
	for val in l1[1:]:
		temp.next = Node(val)
		temp = temp.next
	temp.next = common
	temp = h2
	for val in l2[1:]:
		temp.next = Node(val)
		temp = temp.next
	temp.next = common
	return h1,h2

def printLL(head:Node) -> None:
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next


l1 = [1,2,3]
l2 = [2,3]
common = 3
h1,h2 = createTestSet(l1,l2,common)


# ------------ Brute Force using Set -------------

# def bruteForce(h1:Node,h2:Node) -> Node | None:
# 	if h1 is None or h2 is None:
# 		return None
# 	st = set()
# 	temp = h1
# 	while temp:
# 		st.add(temp)
# 		temp = temp.next
# 	temp = h2
# 	while temp:
# 		if temp in st:
# 			return temp
# 		temp = temp.next
# 	return None

# res = bruteForce(h1,h2)
# print(res.data)



# ----------- Optimal Soln --------------

def optimalSoln(h1:Node,h2:Node) -> Node | None:
	d1,d2 = h1,h2
	while d1 != d2:
		d1 = d2 if d1 is  None else d1.next
		d2 = d1 if d2 is None else d2.next
	return d1



	




