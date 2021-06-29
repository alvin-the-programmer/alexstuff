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

# "in place" means do not copy the list, we want to mutate the original

# a (h) -> b -> c -> d (t)
# prev = c
# d.next = prev
# prev.next = b
# [a,b,c,d]

# V1: store nodes in an array for reference

# def reversell(head):
#     arr = []
#     while head:
#         arr.append(head)
#         head = head.next
#     i = len(arr) - 1

#     while i > 0:
#         curr = arr[i]
#         curr.next = arr[i - 1]
#         i -= 1
#         print(curr.val)

#     if i == 0:
#         arr[i].next = None
#     return arr[-1]

# V2: without using an array


# a < - b -> c

# prev = a
# curr = b
# temp = b


def reversell(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

# a -> b -> c
# want c -> b -> a

def recur_reversell(head, prev = None):
    if not head:
        return prev # c
        
    next_node = head.next # b / c / none 
    head.next = prev # a -> none / b -> a / c -> b
    return recur_reversell(next_node, head) # (b, a)/ (c, b) / (none, c)
    

# space : O(1)

print_list(recur_reversell(head))



#
#
#
##
##
#
#
#
#
#
#
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


def reverse_linked_list(head, prev=None):
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


