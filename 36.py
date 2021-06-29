# https://awwapp.com/b/uo8byidyrb4n0/
# ttps://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        first = preorder[0]
        root = TreeNode(first)

        mid = inorder.index(first)

        leftInorder = inorder[:mid]
        left = self.buildTree(preorder[1:len(leftInorder) + 1], leftInorder)
        right = self.buildTree(preorder[len(leftInorder) + 1:], inorder[mid+1:])

        root.left = left
        root.right = right
        return root