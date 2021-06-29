
# pre: self, left, right
# in: left, self, right
# post: left, right, self

# Input: 
# inorder = [9,3,15,20,7], 
#     l_inorder = [a,b,c]
#                 [a,c,b]
#     r_inorder = [15,20,7]
# postorder = [9,15,7,20,3]
#    l_post: 
# Output: 
# [3,9,20,null,null,15,7]

from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.buildTreeHelper(inorder, postorder)
        
    def buildTreeHelper(self, inorder, postorder):
        if not inorder and not postorder:
            return None
        
        curr_val = postorder.pop()
        curr_node = TreeNode(curr_val)
        curr_inorder_idx = inorder.index(curr_val)
        l_inorder = inorder[:curr_inorder_idx]
        r_inorder = inorder[curr_inorder_idx+1:]
        l_postorder = postorder[:len(l_inorder)]
        r_postorder = postorder[len(l_postorder):]
        
        curr_node.left = self.buildTreeHelper(l_inorder, l_postorder)
        curr_node.right = self.buildTreeHelper(r_inorder, r_postorder)

        return curr_node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [0 1 2 3]
class Solution:
  def flatten(self, root):
      if root is None:
        return []
        
      stack = [root]
      prev = None
      while stack:
        curr = stack.pop()

        if curr.right is not None:
          stack.append(curr.right)

        if curr.left is not None:
          stack.append(curr.left)

        curr.left = None
        if prev is not None:
          prev.right = curr
        prev = curr
      return root

    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if root is None:
    #       return None
    #     order = []
    #     self.df_traversal(root, order)

    #     for idx in range(1, len(order)):
    #       prev_node = order[idx - 1]
    #       node = order[idx]

    #       prev_node.left = None
    #       prev_node.right = node

    #     order[-1].left = None
    #     order[-1].right = None

    #     return root


    # def df_traversal(self, root, order):
    #   if root is None:
    #     return
      
    #   order.append(root)

    #   self.df_traversal(root.left, order)
    #   self.df_traversal(root.right, order)

    # def df_traversal(self, root):
    #   stack = [root]

    #   order = []
    #   while stack:
    #     curr = stack.pop()
    #     order.append(curr)
       
    #     if curr.right is not None:
    #       stack.append(curr.right)

    #     if curr.left is not None:
    #       stack.append(curr.left)
    #   return order

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
          return [[1]]

        pre_output = self.generate(numRows - 1)
        curr_row = []
        
        for i in range(numRows):
          if i == 0 or i == (numRows - 1):
            curr_row.append(1)
          else:
            last_row = pre_output[-1]
            curr_row.append(last_row[i - 1] + last_row[i])

        pre_output.append(curr_row)
        return pre_output
        
numRows = 3
self.generate(numRows - 1) = [[1],[1,1]]

# flatten bt 
# pascals iteratively

# "aaabbbc"