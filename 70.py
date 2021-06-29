# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        alt_path = [0]
        self.max_level(root, alt_path)
        return alt_path[0]

    def max_level(self, root, alt_path):
        if root is None:
            return 0

        left = self.max_level(root.left, alt_path)
        right = self.max_level(root.right, alt_path)

        if left + right > alt_path[0]:
            alt_path[0] = left + right

        return 1 + max(left, right)

    
# alt_path: 5
#         

#         (a)
#      3/     \2
#     (b)       c
#   2 / \1      \    
#   (d)  e       f
#  1/    \
#  (g)   \
#         \
#         \
#        \
# DF_trav(longest)


