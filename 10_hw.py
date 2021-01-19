class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

a = Node(3)
b = Node(7)
c = Node(2)
d = Node(10)
e = Node(3)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
root = a
#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4


# [1] Write a fn `tree_sum(root)` that takes in the root of a binary tree that contains
# numbers as node values. The fn should return the total sum of values in the tree.
#
# Build two solutions: one iterative, one recursive.
#
#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#
# tree_sum(root) # 29


# [2] Write a fn `tree_contains(root, targetVal)` that takes in the root of a binary tree and a
# value. The fn should return a boolean indicating whether the tree contains the value.
#
# Build two solutions: one iterative, one recursive.
#
#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#
# tree_contains(root, 3) # true
# tree_contains(root, 10) # true
# tree_contains(root, 2) # true
# tree_contains(root, 5) # false
# tree_contains(root, 1) # false


# [3] Write a fn `tree_max(root)` that takes in the root of a binary tree with number values.
# The fn should return the maximum value within the tree.
#
# Build two solutions: one iterative, one recursive.
#
#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#
# tree_max(root) # 10


# [4] LeetCode102 https://leetcode.com/problems/binary-tree-level-order-traversal/