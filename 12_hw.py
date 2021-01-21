# leetcode#101 - https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
class Solution:
       def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.check(root.left, root.right)
    
    def check(self, left_sub, right_sub):
        if left_sub is None and right_sub is None:
            return True
        if left_sub is not None and right_sub is not None:
            return left_sub.val == right_sub.val and self.check(left_sub.left, right_sub.right) and self.check(left_sub.right, right_sub.left)
        
        return False
    
# leetcode#111 - https://leetcode.com/problems/minimum-depth-of-binary-tree/
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # for the case that we are given an EMPTY tree
        if root is None:
            return 0
        
        return self.minDepthHelper(root)
    
    def minDepthHelper(self, root):
        if root is None:
            return float(inf)
        if root.left is None and root.right is None:
            return 1
        
        # only return when we have found a LEAF
        return min(1 + self.minDepthHelper(root.left), 1 + self.minDepthHelper(root.right))

# leetcode#226 - https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        
        return root
    