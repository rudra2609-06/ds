from typing import List
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


def printLL(head:Node):
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next


def lenLL(head:Node) -> int:
	temp = head
	cnt = 0
	while temp:
		cnt += 1
		temp = temp.next
	return cnt

def initializeSLL(arr:List[int]) -> Node:
	n = len(arr)
	if n <= 0:
		return None
	head = Node(arr[0])
	temp = head
	for i in range(1,n):
		newNode = Node(arr[i])
		temp.next = newNode
		temp = temp.next
	return head




# ---------- deletion of head ----------

# def deleteHead(head:Node) -> Node:
# 	temp = head
# 	newHead = temp.next
# 	head.next = None
# 	return newHead


# res = deleteHead(n1)
# printLL(res)


# ---------- deletion of tail ----------

# def deleteTail(head:Node) -> Node:
# 	temp = head
# 	while True:
# 		if not temp.next.next:
# 			break
# 		temp = temp.next
# 	newTail = temp
# 	temp.next = None
# 	return head

# res = deleteTail(n1)
# printLL(res)

# ---------- deletion of kth Element (1-based-indexing) ----------

def deleteKth(head:Node,k:int) -> Node:
	if head is None:
		return head
	ln = lenLL(head)
	if k > ln:
		return None
	if k == 1:
		newHead = head.next
		head.next = None
		return newHead
	cnt = 1
	temp = head
	while True:
		if cnt == (k - 1):
			break
		temp = temp.next
		cnt += 1
	nextEl = temp.next
	temp.next = temp.next.next
	nextEl.next = None
	return head
	
# res = deleteKth(n1,4)
# printLL(res)
		
# -------------------- deletion of Basis Of Value --------------------

def deleteElOnValue(head:Node,el:int) -> Node:
	if head is None or el <= 0:
		return head
	if head.data == el:
		newHead = head.next
		return newHead
	prev = None
	temp = head
	while temp.data != el:
		prev = temp
		temp = temp.next
	prev.next = prev.next.next
	return head


# res = deleteElOnValue(n1,0)
# printLL(res)


# -------------------- insertion at head --------------------

def insertionAtHead(head:Node,el:int) -> Node:
	if head is None:
		return head
	newHead = Node(el)
	newHead.next = head
	return newHead

# res = insertionOfHead(n1,0)
# printLL(res)

# -------------------- insertion at tail --------------------

def insertionAtTail(head:Node,el:int) -> Node:
	if head is None:
		return head
	temp = head
	while temp.next is not None:
		temp = temp.next
	newTail = Node(el)
	temp.next = newTail
	return head

# res = insertionAtTail(n1,5)
# printLL(res)


# -------------------- insertion at kth Position --------------------


def insertionAtKth(head:Node,el:int,k:int) -> Node:
	if head is None or k <= 0:
		return head
	ln = lenLL(head)
	# insert at head
	if k == 1:
		newHead = Node(el)
		newHead.next = head
		return newHead
	# insert at tail
	elif k == (ln + 1):
		temp = head
		while temp.next is not None:
			temp = temp.next
		newTail = Node(el)
		temp.next = newTail
		return newTail
	# insert b/w head and tail
	else:
		cnt = 1
		temp = head
		while cnt != (k - 1):
			temp = temp.next
			cnt += 1
		newEl = Node(el)
		newEl.next = temp.next
		temp.next = newEl
		return head

# res = insertionAtKth(n1,0.5,2)
# printLL(res)

		

# -------------------- insertion before given node --------------------


def insertBeforeGivenVal(head:Node,el:int,val:int) -> Node:
	if head is None:
		return head
	# insert before head i.e. new head
	if head.data == val:
		newHead = Node(el)
		newHead.next = head
		return newHead
	prev = None
	curr = head
	while curr.data != val:
		prev = curr
		curr = curr.next
	newEl = Node(el)
	newEl.next = prev.next
	prev.next = newEl
	return head

# res = insertBeforeGivenVal(n1,0.5,3)
# printLL(res)



# --------------- Add 2 LL ---------------

# arr1 = [5, 4]
# arr2 = [4]

# h1 = initializeSLL(arr1)
# h2 = initializeSLL(arr2)

def add2LL(h1:Node,h2:Node) -> Node:
	if h1 is None:
		return h2
	if h2 is None:
		return h1
	dummyNode = Node(-1)
	curr = dummyNode
	t1 = h1
	t2 = h2
	carry = 0
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
	if carry > 0:
		newNode = Node(carry)
		curr.next = newNode
		curr = curr.next
	return dummyNode.next

# res = add2LL(h1,h2)
# printLL(res)



# --------------- Group Odd And Even ---------------

# arr = [4, 3, 2, 1]
# head = initializeSLL(arr)

def groupOddAndEven(head:Node) -> Node:
	odd = Node(-1)
	sender = odd
	even = Node(-1)
	connector = even
	cnt = 1
	temp = head
	while temp:
		# add to even chain
		if cnt % 2 == 0:
			newNode = Node(temp.data)
			even.next = newNode
			even = even.next
		# add to odd chain
		else:
			newNode = Node(temp.data)
			odd.next = newNode
			odd = odd.next
		temp = temp.next
		cnt += 1
	odd.next = connector.next
	return sender.next


# res = groupOddAndEven(head)
# printLL(res)



# --------------- remove-nth-node-from-back ---------------

def removeNthNodeFromBack(head:Node,n:int) -> Node:
	if head is None:
		return None
	if head.next is None and n == 1:
		return None

	slow = head
	fast = head
	while n != 0:
		fast = fast.next
		n -= 1

	if not fast:
		newHead = head.next
		return newHead


	while fast.next is not None:
		slow = slow.next
		fast = fast.next
	old = slow.next
	slow.next = slow.next.next
	old.next = None
	return head

# head = initializeSLL([1,2,3,4,5])
# res = removeNthNodeFromBack(head,5)
# printLL(res)



# --------------- sort 0's/1's/2's ---------------

def sort0s1s2s(head:Node) -> Node:
	if head is None or head.next is None:
		return head
	
	dummyZero = Node(-1)
	d0 = dummyZero
	dummyOne = Node(-1)
	d1 = dummyOne
	dummyTwo = Node(-1)
	d2 = dummyTwo

	temp = head
	while temp:
		if temp.data == 0:
			dummyZero.next = temp
			dummyZero = dummyZero.next
		elif temp.data == 1:
			dummyOne.next = temp
			dummyOne = dummyOne.next
		else:
			dummyTwo.next = temp
			dummyTwo = dummyTwo.next
		temp = temp.next

	dummyZero.next = d1.next if d1.next else d2.next
	dummyOne.next = d2.next 
	dummyTwo.next = None
	head = d0.next
	return head

# res = sort0s1s2s(initializeSLL([1, 0, 2, 0 , 1]))
# printLL(res)


# --------------- reverseLL ---------------

def reverseLL(head:Node) -> Node:
	if head is None or head.next is None:
		return None
	prev = None
	curr = head
	while curr:
		nextEl = curr.next
		curr.next = prev
		prev = curr
		curr = nextEl
		
	return prev

# res = reverseLL(initializeSLL([1,2,3,4,5]))
# printLL(res)


# --------------- add no. 1 to LL ---------------

def addOneToLL(head:Node) -> Node:
	if head is None or head.next is None:
		return head

	# reverse in order to add
	rvHead = reverseLL(head)
	temp = rvHead
	carry = 1
	while rvHead:
		total = rvHead.data + carry
		carry = total // 10
		rvHead.data = total % 10
		rvHead = rvHead.next
	

	rvHead = reverseLL(temp)
	if carry == 1:
		newHead = Node(carry)
		newHead.next = rvHead
		return newHead
	return rvHead

# res = addOneToLL(initializeSLL([1,9,8]))
# printLL(res)
	
	

# --------------- find the middle LL ---------------

def findTheMiddleOfLL(head:Node) -> Node:
	if head is None or head.next is None:
		return head
	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow.data

# res = findTheMiddleOfLL(initializeSLL([3,8,7,1,3]))
# res = findTheMiddleOfLL(initializeSLL([2,9,1,4,0,4]))
# print(res)

# --------------- delete the middle node LL ---------------


def deleteTheMiddleOfLL(head:Node) -> Node:
	if head is None or head.next is None:
		return head
	slow = head
	fast = head
	prev = None
	while fast and fast.next:
		prev = slow
		slow = slow.next
		fast = fast.next.next
	nodeToDel = prev.next
	prev.next = nodeToDel.next
	nodeToDel.next = None
	return head

# res = deleteTheMiddleOfLL(initializeSLL([7,6,5,4]))
# res = deleteTheMiddleOfLL(initializeSLL([1,2,3,4,5]))
# printLL(res)

# --------------- check palindrome ---------------

def checkPalindrome(head: Node) -> bool:
    if head is None or head.next is None:
        return True

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    revHead = reverseLL(slow.next)   # second half, reversed
    second = revHead
    first = head

    result = True
    while second:
        if first.data != second.data:
            result = False
            break
        first = first.next
        second = second.next

    slow.next = reverseLL(revHead)   # restore the original list
    return result

# res = checkPalindrome(initializeSLL([3,7,5,2,3]))
# print(res)

# -------------------- sort LL --------------------

def findMid(head:Node) -> Node:
	slow = head
	fast = head.next
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow


def merge2SortedArrs(h1:Node,h2:Node) -> Node:
	d1,d2 = h1,h2
	dummyNode = Node(-1)
	d = dummyNode
	while d1 and d2:
		if d1.data <= d2.data:
			dummyNode.next = d1
			d1 = d1.next
		else:
			dummyNode.next = d2
			d2 = d2.next
		dummyNode = dummyNode.next
	while d1:
		dummyNode.next = d1
		d1 = d1.next
	while d2:
		dummyNode.next = d2
		d2 = d2.next
	return d.next


def sortLL(head:Node) -> Node:
	if head is None or head.next is None:
		return head

	mid = findMid(head)
	left = head
	right = left.next
	left.next = None
	l = sortLL(left)
	r = sortLL(right)
	return merge2SortedArrs(l,r)


# res = sortLL(initializeSLL([5,4,3,2,1]))
# printLL(res)	


# ------------ rotate the ll right n times ------------

def rotateNTimesRight(head:Node,k : int) -> Node:
	if head is None or head.next is None:
		return head

	ln = lenLL(head)
	
	newHead = head
	while ( k % ln ) != 0:
		temp = newHead
		while temp.next.next is not None:
			temp = temp.next
		temp.next.next = newHead
		newHead = temp.next
		temp.next = None
		k -= 1
	return newHead

res = rotateNTimesRight(initializeSLL([1,2,3,4,5]),1)
printLL(res)



	







	

	
	




	


	




	
	
	




	




