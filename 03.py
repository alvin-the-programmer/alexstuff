class Node:
 def __init__(self, val):
  self.next = None
  self.val = val



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d
head = a

def print_list(head):
 if head == None:
  return
 print(head.val)
 print_list(head.next)

# Write a fn that takes in the head of a LL and reverses the order of the nodes in-place.

# n = # nodes
# time: O(n)
# space: O(1)
# def reverse_linked_list(head):
#     curr = head
#     prev = None
#     while curr != None:
#         temp = curr.next
#         curr.next = prev

#         prev = curr
#         curr = temp
#     return prev



# n = # nodes
# time: O(n)
# space: O(n)
# def reverse_linked_list(head):
#   return reverse_linked_list_helper(head, None)

# def reverse_linked_list_helper(head, prev):
#   if head == None:
#     return prev
#   temp = head.next
#   head.next = prev
#   return reverse_linked_list_helper(temp, head)




def reverse_linked_list(head, prev = None):
  if head == None:
    return prev
  temp = head.next
  head.next = prev
  return reverse_linked_list(temp, head)

# cu curr
# p prev
# t temp


#               p  cu   
# <- a <- b  <- c  NONE

# print_list(head)
# print('---')
# new_head = reverse_linked_list(head)
# print_list(new_head) 




# https://awwapp.com/b/ucf8kv371dmdp/