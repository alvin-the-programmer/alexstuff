
# Binary Search Trees
#  Binary Tree where given any 'subroot' all values to the left are < the subroot
#  and all values to the right are >= the subroot


# https://awwapp.com/b/umvtc6wn1loxl/


# "Depth First Traversal"
#  - preorder
#  - inorder
#  - postorder


# class Node:
#   def __init__(self,val):
#     self.val = val
#     self.left = None
#     self.right = None

# a = Node(64)
# b = Node(30)
# c = Node(64)
# d = Node(25)
# e = Node(32)
# f = Node(65)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

#      64
#    /   \
#   30    64
#   / \    \
#  25   32  65


# preorder: self, left, right
def preOrderPrint(root):
  if root is None:
    return
  
  print(root.val)
  preOrderPrint(root.left)
  preOrderPrint(root.right)


# preOrderPrint(a)
# 64
# 30
# 25
# 32
# 64
# 65


# inorder: left, self, right
def inOrderPrint(root):
  if root is None:
    return
  
  inOrderPrint(root.left)
  print(root.val)
  inOrderPrint(root.right)


#      64
#    /   \
#   30    64
#   / \    \
#  25   32  65

# inOrderPrint(a)
# 25
# 30
# 32
# 64
# 64
# 65

# postorder: left, right, self


# Write a fn that takes in a bst and returns an array containing all values of the bst in increasing order.

# inOrderValues(a)
# [ 25, 30, 32, 64, 64, 65 ]

def inOrderValues(root):
    if root is None:
        return []
    
    return inOrderValues(root.left) + [root.val] + inOrderValues(root.right)

class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

a = Node(64)
b = Node(30)
c = Node(64)
d = Node(25)
e = Node(32)
f = Node(65)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      64
#    /   \
#   30    64
#   / \    \
#  25   32  65

# print(inOrderValues(a))
# [ 25, 30, 32, 64, 64, 65 ]




# binarySearchTreeFind(a, 32) # true
# binarySearchTreeFind(a, 30) # true
# binarySearchTreeFind(a, 31) # false

def binarySearchTreeFind(curr, val):
    if curr is None:
        return False

    if curr.val == val:
        return True
    
    if curr.val > val:
        return binarySearchTreeFind(curr.left, val)
    else: 
        return binarySearchTreeFind(curr.right, val)


print(binarySearchTreeFind(a, 32)) # true
print(binarySearchTreeFind(a, 30)) # true
print(binarySearchTreeFind(a, 31)) # false

# Worst Case BinarySearchTree#find: O(n) time, n = # nodes


# Balanced Tree
#  - "best case"
#  - "shortest tree that fits n nodes"
#  - tree where given any subroot, the heights b/w the left and right subtrrees differ <= 1

# Balanced tree of n nodes has height ~ log(n)
