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
c.right = f
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

# depth first since we need a recursive solution
# iterative
# n = # of nodes in tree
# time = O(n)
# space = O(n)
# def tree_sum(root):
#   total = 0
#   stack = [root]
#   while len(stack) != 0:
#     top = stack.pop()
#     total += top.val
#     if top.right is not None:
#       stack.append(top.right)
#     if top.left is not None:
#       stack.append(top.left)
#   return total

# n = number of nodes in tree
# time: O(n)
# space: O(n) for each call on the call stack for each node in the tree
# def tree_sum(root):
#   # base case

#   if root == None:
#     return 0
#   # go down left side first each time
#   return root.val + tree_sum(root.left) + tree_sum(root.right)



# print(tree_sum(root))

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

# must we always PUSH to a stack BEFORE doing the CHECK on their values? Or is there a way to check it while we walk through?

# DFS
# n is number of nodes in tree
# Time: O(n)
# space: O(n) to hold each node in the stack
# def tree_contains(root, targetVal):
#   stack = [root]
#   while len(stack) != 0:
#     top = stack.pop()
#     if top.val == targetVal:
#       return True
#     if top.right != None:
#       stack.append(top.right)
#     if top.left != None:
#       stack.append(top.left)
#   return False

# DFS
# Time: O(n)
# Space: O(n)
# def tree_contains(root, targetVal):
#   if root == None:
#     return False
#   if root.val == targetVal:
#     return True
#   # we need to always check both sides, but one side could be false and another could be true, so use an OR condition and wait for the entire expression to evaluate before returning
#   return tree_contains(root.left, targetVal) or tree_contains(root.right, targetVal)

# print(tree_contains(root, 3)) # true
# print(tree_contains(root, 10)) # true
# print(tree_contains(root, 2)) # true
# print(tree_contains(root, 5)) # false
# print(tree_contains(root, 1)) # false


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
# DFS
# Time: O(n)
# Space: O(n)
# def tree_max(root):
#   max = float('-inf')
#   stack = [root]
#   while len(stack) != 0:
#     top = stack.pop()
#     if top.val > max:
#       max = top.val
#     if top.right != None:
#       stack.append(top.right)
#     if top.left != None:
#       stack.append(top.left)
#   return max

# Time: O(n)
# Space: O(n)
def tree_max(root):
  if root == None:
    return float('-inf')
  return max(root.val, tree_max(root.left), tree_max(root.right))


# a = Node(-3)
# b = Node(-7)
# c = Node(-2)
# d = Node(-10)
# e = Node(-3)
# f = Node(-4)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# root = a

# print(tree_max(root)) # 10

# [4] LeetCode102 https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if root == None:
    #         return []
    #     # DFS
    #     final = []
    #     first_obj = {
    #         'node': root,
    #         'depth': 0
    #     }
    #     stack = [first_obj]
    #     while len(stack) != 0:
    #         top = stack.pop()
            
    #         if len(final) > top['depth']:
    #             final[top['depth']].append(top['node'].val)
    #         else:
    #             final.append([top['node'].val])
            
    #         if top['node'].right != None:
    #             right_obj = {
    #                 'node': top['node'].right,
    #                 'depth': top['depth'] + 1
    #             }
    #             stack.append(right_obj)
    #         if top['node'].left != None:
    #             left_obj = {
    #                 'node': top['node'].left,
    #                 'depth': top['depth'] + 1
    #             }
    #             stack.append(left_obj)
    #     return final

    #   def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if root == None:
    #         return []
    #     # DFS
    #     final = []
    #     stack = [ ( root, 0 ) ]
    #     while len(stack) != 0:
    #         curr, depth = stack.pop()
            
    #         if len(final) > depth:
    #             final[depth].append(curr.val)
    #         else:
    #             final.append([curr.val])
          
    #         if curr.right != None:
    #             stack.append(( curr.right, depth + 1 ))
    #         if curr.left != None:
    #             stack.append(( curr.left, depth + 1 ))
    #     return final
      
    #   def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if root == None:
    #         return []
    #     # DFS
    #     final = []
    #     queue = [ ( root, 0 ) ]
    #     while len(queue) != 0:
    #         curr, depth = queue.pop()
            
    #         if len(final) > depth:
    #             final[depth].append(curr.val)
    #         else:
    #             final.append([curr.val])
          
    #         if curr.left != None:
    #             queue.insert(0,( curr.left, depth + 1 ))
    #         if curr.right != None:
    #             queue.insert(0,( curr.right, depth + 1 ))
    #     return final
class Solution:


  def levelOrder(self, root):
    final = []
    self.traverse(root, 0, final)
    return final

  def traverse(self, root, depth, final):
    if root == None:
      return
    
    if len(final) > depth:
      final[depth].append(root.val)
    else:
      final.append([root.val])

    self.traverse(root.left, depth + 1, final)
    self.traverse(root.right, depth + 1, final)

s = Solution()
# print(s.levelOrder(root))


# Binary Trees
#  - tree where every node has at most two children


# Binary Search Tree
# - type of binary tree
# - at any node, all children to the left of that node are <, and all children to the right are >


#        20
#       /  \
#      10    25 
#    /  \
#   2    19

