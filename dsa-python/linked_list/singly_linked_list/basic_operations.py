class Node:
	def __init__(self,data):
		self.data = data
		self.next = None



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4


# -------------  calculate the lenght of linked list ----------

# temp = head

# cnt = 0

# while temp:
# 	if temp.next == None:
# 		cnt += 1
# 		break
# 	cnt += 1
# 	temp = temp.next 

# print(cnt)
		

# -------------  search inside linked list ----------

head = n1
element = 1

isPresent = False
temp = head

while temp:
	if temp.data == element:
		isPresent = True
		break
	temp = temp.next

print(isPresent)


