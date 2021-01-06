class Node:
 def __init__(self, val):
  self.next = None
  self.val = val

def print_list(head):
 if head == None:
  return
 print(head.val)
 print_list(head.next)

# [1] Write a fn push(head, val) that takes in a linked list and a value.
# The fn should add a new node to the end of the linked list with the given value.
head = Node('a')
head.next = Node('b')
head.next.next = Node('c')
head.next.next.next = Node('x')
head.next.next.next.next = Node('y')

def push(head, val):
  add_to_end(head.next, val)
  return head

def add_to_end(node, val):
  if node.next == None:
    new_node = Node(val)
    node.next = new_node
    return
  return add_to_end(node.next, val)

# head = a -> b -> c
# print_list(push(head, 'x')) # a -> b -> c -> x
# print_list(push(head, 'y')) # a -> b -> c -> x -> y

# [2] Write a fn insert(head, val, targetIdx) that takes in a linked list, a value, and an index.
# The fn should insert a new node containing the value into the linked list, at the given index.
# Consider the head of the linked list as having index 0.
#

# pseudo
# make a recursive helper method which will traverse the linked list
# this helper method should return the node ONE BEFORE the given index
# once we have the node at given index, all we need to do is insert a new node
# make a copy of the NEXT node
# have the PREVIOUS node point to the new node
# have the new node point to the NEXT node

def insert(head, val, targetIdx):
  new_node = Node(val)
  prev_node = find_node_before_given_idx(head, targetIdx - 1, 0)
  temp = prev_node.next
  prev_node.next = new_node
  new_node.next = temp
  return head

def find_node_before_given_idx(head, targetIdx, currIdx):
  if currIdx == targetIdx:
    return head
  return find_node_before_given_idx(head.next, targetIdx, currIdx + 1)

# head = a -> b -> c -> x -> y 
insert(head, 's', 2) # a -> b -> s -> c -> x -> y 
# print_list(insert(head, 's', 5)) # a -> b -> s -> c -> x -> s -> y 

# [3] Write a fn remove(head, targetVal) that takes in a linked list and a target value.
# The fn should remove and return the first node of the linked list that contains the target value.
# If there is no node that contains the targetVal, then return None.

# if target is the first node, head needs to be set to the second node, but the function says to only return the node at which it occurs?
# if the target is the last node, the node before the last one should point to None

def remove(head, target_val, prev = None):
  if head != None:
    if head.val == target_val:
      if prev != None:
        prev.next = head.next
      return head
  else:
    return None
  prev = head
  return remove(head.next, target_val, prev)

# head = a -> b -> s -> c -> x -> s -> y 
print(remove(head, 'w')) # <Node object s>
print_list(head) # a -> b -> c -> x -> s -> y 
