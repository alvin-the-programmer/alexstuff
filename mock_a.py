# Write a fn that takes in a linked list where the node vals are chars. The fn also takes in as a second 
# arg, a targetString.
# The fn should return a bool indicating whether or not the targetString is contained in the linked
# list, starting at the head.

# list: r->o->a->d , target: 'road'  -> true
# list: r->o->a->d , target: 'ro'  -> true
# list: r->o->a->d , target: 'roads'  -> false
# list: r->o->a->d , target: 'ra'  -> false

class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None

def has_linked_list_prefix(head, target_string):
    # if empty string, its always true
    if target_string == '':
        return True
    # if head is none but we still have characters to look for, this is an edge case
    if head is None and target_string != "":
        return False
    
    # check each letter and keep traversing
    if head.val == target_string[0]:
        return has_linked_list_prefix(head.next, target_string[1:])
    else:
        return False
    
r = None
o = Node('o')
a = Node('a')
d = Node('d')

# r.next = o
o.next = a
a.next = d

# print(has_linked_list_prefix(r,''))

# Write a fn that takes in the root of a bin tree and a targetStr.targetStr.
# The fn should return the number of paths in the tree that start at the root and represent
# the targetStr.

#          p  
#       /     \
#      l       a 
#     / \     / \
#    a   y   i   n 
#     \      \
#      n     n


# prefix_path_count(root, 'ply') # 1
# prefix_path_count(root, 'pan') # 1
# prefix_path_count(root, 'plys') # 0
# prefix_path_count(root, 'pl') # 1

#          p  
#       /     \
#      l       l 
#     / \     / \
#    a   y   y   n 
#     \      \
#      n     n

class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

p = Node('p')
l1 = Node('l')
l2 = Node('l')
a = Node('a')
y1 = Node('y')
y2 = Node('y')
n1 = Node('n')
n2 = Node('n')
n3 = Node('n')

p.left = l1
p.right = l2
l1.left = a
l1.right = y1
l2.left = y2
l2.right = n1
a.right = n2
y2.right = n3
#          p  
#       /     \
#      l       l 
#     / \     / \
#    a   y   y   n 
#     \      \
#      n     n


def prefix_path_count(root, target_string):
    # solely here for the case that we are initially given an empty string?
    if target_string == "":
        return 1
    if root is None:
        return 0
    
    if root.val == target_string[0]:
        # preemptively check if we have already finished our word
        if target_string[1:] == "":
            return 1
        else:
            return prefix_path_count(root.left, target_string[1:]) + prefix_path_count(root.right, target_string[1:])
    else:
        return 0

print(prefix_path_count(p, 'ply')) # 2
print(prefix_path_count(p, 'pln')) # 1
print(prefix_path_count(p, 'p')) # 1
print(prefix_path_count(None, '')) # 1






