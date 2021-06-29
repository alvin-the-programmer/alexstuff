class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

# a = Node(3)
# b = Node(7)
# c = Node(2)
# d = Node(10)
# e = Node(3)
# f = Node(4)
# x = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = x
# root = a

#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#    /
#   1

# Write a function that takes in a bintree as an arg and returns the max sum of any root to leaf path
# of the tree. 
# Assume the tree only contains positive ints.


#       3
#     /  \
#    7    2 
#  / \     \
# 10  11     4
#    /
#   1

def max_path_sum(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val

    left = max_path_sum(root.left)
    right = max_path_sum(root.right)
    return root.val + max(left, right)



a = Node(-3)
b = Node(-7)
c = Node(-2)
d = Node(-10)
e = Node(-11)
f = Node(-4)
x = Node(-1)


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = x
root = a

#       -3
#     /  \
#   - 7    -2 
#  / \     \
# -10  -11     -4
#    /
#   -1

# print(max_path_sum(root)) # 


def max_path_sum(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val

    left = max_path_sum(root.left)
    right = max_path_sum(root.right)
    return root.val + max(left, right)


def tree_height(root):
    if root is None:
        return -1
    if root.left is None and root.right is None:
        return 0
    
    left = tree_height(root.left)
    right = tree_height(root.right)

    return 1 + max(left, right)

print(tree_height(root))

# https://awwapp.com/b/uxo5blbloyimq/