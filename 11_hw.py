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
x = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = x
root = a

#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#    /
#   1



# [1] Write a fn has_path_sum that takes in the root of a bintree and a targetSum as arguments.
# The fn should return a boolean indicating whether or not there is some path whose sum
# of values is the targetSum. 
# A path must begin at the root, but does *not* need to end at a leaf.
# You can assume the node values are always positive numbers.
#
#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#    /
#   1
#

# DFS
def has_path_sum(root, target_sum):
  return has_path_sum_helper(root, target_sum, 0)

def has_path_sum_helper(root, target_sum, curr_sum):
  if root is None:
    return False
  
  curr_sum = curr_sum + root.val
  if curr_sum == target_sum:
    return True
    
  return has_path_sum_helper(root.right, target_sum, curr_sum) or has_path_sum_helper(root.left, target_sum, curr_sum)


# print(has_path_sum(root, 9)) # true
# print(has_path_sum(root, 5)) # true
# print(has_path_sum(root, 13)) # true
# print(has_path_sum(root, 2) )# false
# print(has_path_sum(root, 1) )# true

# [2] Write a fn any_path_sum that takes in the root of a bintree and a targetSum as arguments.
# The fn should return a list representing the  path whose sum of values is the targetSum. 
# If there is no such path, then return an empty list.
# A path must begin at the root, but does *not* need to end at a leaf.
# You can assume the node values are always positive numbers.
#
#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#    /
#   1
#
# any_path_sum(root, 9) # [ 3, 2, 4 ]
# any_path_sum(root, 5) # [3, 2]
# any_path_sum(root, 13) # [3, 7, 3]
# any_path_sum(root, 10) # []
# any_path_sum(root, 9) # []

def 

# [3] LeetCode#112 (https://leetcode.com/problems/path-sum/)

# [4] Leetcode#113 (https://leetcode.com/problems/path-sum-ii/)




