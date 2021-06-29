# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def verticalOrder(self, root):
        if root is None:
          return []

        column_dict = {}
        self.bf_traverse(root, column_dict)
        start = min(column_dict.keys())
        output = []
        while start in column_dict:
            output.append(column_dict[start])
            start += 1
        return output


    def bf_traverse(self, root, column_dict):
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            
            if column not in column_dict:
                column_dict[column] = []
            column_dict[column].append(node.val)

            if node.left is not None:
                queue.append((node.left, column - 1))
            if node.right is not None:
                queue.append((node.right, column + 1))
                
