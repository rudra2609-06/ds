# # you are given a ll which has a cycle in it such that you need to return the node where the loop started it no loop there return None



# optimal code
# if head is None:
#             return None
#         temp = head
#         fast = head
#         slow = head
#         hasLoop = False
#         while fast is not None and fast.next is not None:
#             fast = fast.next.next
#             slow = slow.next

#             if fast == slow:
#                 hasLoop = True
#                 break
#         if not hasLoop:
#             return None
#         else:
#             while temp != slow:
#                 temp = temp.next
#                 slow = slow.next
#             return temp