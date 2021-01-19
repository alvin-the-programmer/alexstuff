 # https://awwapp.com/b/umt6khvyu3pa5/

# Graph
#    - collection of nodes and edges
# Tree
#    - is a graph
#    - there is one root node (the root has no parent)
#    - there is a unique path from the root to every leaf (a leaf has no children)
# Binary Tree
#    - is a tree
#    - each node has at most 2 children



class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       a
#     /  \
#    b    c 
#  / \     \
# d   e    f 


# print all values of a binary tree (iter, recur)
# add all values of b tree


# a level of a tree, is the group of nodes that are all the same distance away from the root

#       a
#     /  \
#    b    c 
#  / \     \
# d   e    f 

# depth-first-traversal
  # abdecf

# breadth-first-traversal
  # abcdef


# https://awwapp.com/b/ueinq04twlckm/

# def depth_first_print(root):
#   stack = []
#   stack.append(root)
#   while len(stack) != 0:
#     temp = stack[-1]
#     print(temp.val)
#     stack.pop()
#     if temp.right != None:
#       stack.append(temp.right)
#     if temp.left != None:
#       stack.append(temp.left)
# n = # of nodes in the tree
# time = O(n)
# space = O(n)
# def depth_first_print(root):
#   if root is None:
#     return

#   stack = [root]
#   while len(stack) != 0:
#     temp = stack.pop()
#     print(temp.val)
    
#     if temp.right != None:
#       stack.append(temp.right)
#     if temp.left != None:
#       stack.append(temp.left)

def depth_first_print(root):
  if root == None:
    return
  print(root.val)
  depth_first_print(root.left)
  depth_first_print(root.right)

depth_first_print(a)
depth_first_print(None)

# def breadth_first_print(root):
#   if root is None:
#     return

#   queue = [root]
#   while len(queue) != 0:
#     temp = queue.pop()
#     print(temp.val)

#     if temp.left != None:
#       queue.insert(0, temp.left)
#     if temp.right != None:
#       queue.insert(0, temp.right)

# breadth_first_print(a)
# breadth_first_print(None)

# abdecf

