# class Node:
#   def __init__(self,val):
#     self.val = val
#     self.left = None
#     self.right = None

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

def any_path_sum(root, target_sum):
  answer = any_path_sum_helper(root, target_sum, 0)
  return answer[::-1]

def any_path_sum_helper(root, target_sum, curr_sum):
  if root is None:
    return []
  curr_sum += root.val
  # first find the NODE that will create the target_sum
  if curr_sum == target_sum:
    return [root.val]

  left_path = any_path_sum_helper(root.left, target_sum, curr_sum)
  # all left side paths will pause here to find a return value first
  if left_path:
    left_path.append(root.val)
    return left_path

  right_path = any_path_sum_helper(root.right, target_sum, curr_sum)
  # all right side paths will pause here to find a return value first
  # if something comes back, then we start appending the node to our array
  if right_path:
    right_path.append(root.val)
    return right_path
  return []

# print(any_path_sum(root, 9)) # [ 3, 2, 4 ]
# print(any_path_sum(root, 5)) # [3, 2]
# print(any_path_sum(root, 13)) # [3, 7, 3]
# print(any_path_sum(root, 10)) # [3, 7]
# print(any_path_sum(root, 40)) # []
# print(any_path_sum(root, 2)) # []


# [3] LeetCode#112 (https://leetcode.com/problems/path-sum/)
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if root is None:
#             return False
#         targetSum = targetSum - root.val
        
#         if root.left is None and root.right is None and targetSum == 0:
#             return True
        
#         return self.hasPathSum(root.right, targetSum) or self.hasPathSum(root.left, targetSum)
            
# [4] Leetcode#113 (https://leetcode.com/problems/path-sum-ii/)
# for one path
# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
#       if root is None:
#         return []
#       if root.left is None and root.right is None and root.val == targetSum:
#         return [[targetSum]]

#       left_paths = self.pathSum(root.left, targetSum - root.val)
#       right_paths = self.pathSum(root.right, targetSum - root.val)
#       all_paths = left_paths + right_paths

#       for path in all_paths:
#         path.insert(0, root.val)

#       return all_paths

  

#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#    /
#   1

# Write a fn that takes in the root of a bintree and returns a 2D list where every sublist represents
# a root to leaf path in the tree

def all_paths(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [[root.val]]

  left = all_paths(root.left)
  right = all_paths(root.right)
  left_and_right = left + right

  for path in left_and_right:
    path.insert(0, root.val)
  
  return left_and_right
  

# print(all_paths(root))
# [
#  [3,7,10],
#  [3,7,3,1],
#  [3,2,4] 
# ]



class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

a = Node('c')
b = Node('a')
c = Node('r')
d = Node('r')
e = Node('t')
f = Node('y')
x = Node('s')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = x
root = a

#       c
#     /  \
#    a    r 
#  / \     \
# r  t     y
#    /
#   s


# Write a fn that takes in the root of  bintree of chars and a word. 
# The fn should return a bool indicating whether or not there is a path through the tree starting at the
# root that constructs the word

def word_path(root, word):
  if root is None:
    return False
  if len(word) == 1 and root.val == word[0]:
    return True
  if word[0] != root.val:
    return False

  left = word_path(root.left, word[1:])
  right = word_path(root.right, word[1:])
  return left or right

print(word_path(root, 'cats')) # true
print(word_path(root, 'car')) # true
print(word_path(root, 'cat')) # true
print(word_path(root, 'crying')) # false