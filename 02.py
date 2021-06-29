# https://awwapp.com/b/ucz6ivcgeexxg/

# linked lists
#   - singly linked list

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


a = Node(4)
b = Node(45)
c = Node(6)
d = Node(-2)
f = Node(6)
e = Node(-2)
a.next = b
b.next = c
c.next = d
f.next = e
h1 = a
h2 = f

# make a method that prints


# def ll(curr):
#     if not curr:
#         return

#     print(curr.val)
#     return ll(curr.next)


def ll(curr):
    while curr:
        print(curr.val)
        curr = curr.next


# ll(a)

# given 2 linked list, add the second list to the first and return the head
# a -> b -> c
# d -> e -> f
# a -> b -> c -> d -> e -> f
# combine_lists(a, d)

def combine_lists(head1, head2):
    # get the tail
    tail = head1
    while tail.next:
        tail = tail.next

    # add head 2 to the tail of head1
    tail.next = head2
    return head1


# 4 -> 45 -> 6 -> None

# Write a fn called print_list(head) that prints out all values within the linked list.

# n = # nodes in the LL
# Time: O(n)
# Space: O(n)


def print_list(head):
    if head == None:
        return
    print(head.val)
    print_list(head.next)


print_list(combine_lists(h1, h2))

# n = # of nodes in the list
# time: O(n)
# space: O(1)
# def print_list(head):
#  curr = head
#  while curr != None:
#   print(curr.val)
#   curr = curr.next

# 4
# 45
# 6

# print_list(a)


# Write a fn called sum_list(head) that takes in a LL of number vals and returns the total sum
# time: O(n)
# space: O(n)
# def sum_list(head):
#  if head == None:
#   return 0
#  return head.val + sum_list(head.next)

# time: O(n)
# space: O(1)
# def sum_list(head):
#  curr = head
#  total_sum = 0
#  while curr != None:
#   total_sum += curr.val
#   curr = curr.next
#  return total_sum

# print(sum_list(a)) # 55


# Write a fn called combine_lists(head1, head2) that takes in two LLs and combines them into one,
# where all the nodes of head1 come before head2


# h1 -> 4 -> 45 -> 6 -> -2
# h2 -> 'a' -> 'b'

# 4 -> 45 -> 6 -> -2 -> 'a' -> 'b'

# def combine_lists(head1, head2):
#  curr = head1
#  while curr.next != None:
#   curr = curr.next
#  curr.next = head2
#  return head1

# n = # nodes in h1,
# time: O(n)
# space: O(n)
def combine_lists(head1, head2):
    head1_tail = get_tail(head1)
    head1_tail.next = head2
    return head1


def get_tail(head):
    if head.next == None:
        return head
    return get_tail(head.next)


h2_a = Node('a')
h2_b = Node('b')
h2_a.next = h2_b

# print_list(combine_lists(h1, h2_a))  # where call helper
