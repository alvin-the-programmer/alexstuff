class Node:
 def __init__(self, val):
  self.next = None
  self.val = val

# [1] Write a fn push(head, val) that takes in a linked list and a value.
# The fn should add a new node to the end of the linked list with the given value.
#
# head = a -> b -> c
# push(head, 'x') # a -> b -> c -> x
# push(head, 'y') # a -> b -> c -> x -> y

# [2] Write a fn insert(head, val, targetIdx) that takes in a linked list, a value, and an index.
# The fn should insert a new node containing the value into the linked list, at the given index.
# Consider the head of the linked list as having index 0.
#
# head = a -> b -> c -> x -> y 
# insert(head, 's', 2) # a -> b -> s -> c -> x -> y 
# insert(head, 's', 5) # a -> b -> s -> c -> x -> s -> y 


# [3] Write a fn remove(head, targetVal) that takes in a linked list and a target value.
# The fn should remove and return the first node of the linked list that contains the target value.
# If there is no node that contains the targetVal, then return None.
#
# head = a -> b -> s -> c -> x -> s -> y 
# remove(head, 's') # <Node object s>
# print_list(head) # a -> b -> c -> x -> s -> y 
