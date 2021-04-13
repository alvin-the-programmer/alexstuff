class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        longest_path = [0]
        
        self.df_trav(root, longest_path)
        
        return longest_path[0]
        
    def df_trav(self, root, longest_path):
        if root is None:
            return 0
        
        left = self.df_trav(root.left, longest_path)
        right = self.df_trav(root.right, longest_path)
        
        new_path = left + right
        
        if new_path > longest_path[0]:
            longest_path[0] = new_path
        
        return 1 + max(left, right)