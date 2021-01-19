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