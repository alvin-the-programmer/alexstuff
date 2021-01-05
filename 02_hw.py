class Node:
 def __init__(self, val):
  self.next = None
  self.val = val


# [1.] Write a fn list_find(head, target) that takes in the head of a LL.
# The fn should return a boolean indicating whether or not the target exists
# as a value in the LL.
#
# Solve iteratively and recursively.
#
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
#
# a.next = b
# b.next = c
# c.next = d
# head = a
# 
# list_find(head, 'c') # True
# list_find(head, 'Z') # False


# [2.] Write a fn list_count(head, target) that takes in the head of a LL.
# The fn should return a number representing the count of that target in the LL.
#
# Solve iteratively and recursively.
# 
# a = Node(1)
# b = Node(3)
# c = Node(7)
# d = Node(3)
# e = Node(1)
# f = Node(1)
#
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# head = a
#
# list_count(head, 1) # 3
# list_count(head, 3) # 2
# list_count(head, 7) # 1
# list_count(head, 42) # 0




