# https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        first_letter = S[0]
        if len(S) == 1:
            if first_letter.isnumeric():
                return [first_letter]
            else:
                return [first_letter.upper(), first_letter.lower()]
        
        permutations = self.letterCasePermutation(S[1:])
        if first_letter.isnumeric():
            for idx in range(len(permutations)):
                permutations[idx] = first_letter + permutations[idx]
        else:
            for idx in range(len(permutations)):
                permutations.append(first_letter.upper() + permutations[idx])
                permutations[idx] = first_letter.lower() + permutations[idx]
        
        return permutations
                
        
# lettCasePermutation('a1b2')
# lcp('1b2')
# [1b2, 1B2]

# https://leetcode.com/problems/balanced-binary-tree/
# https://awwapp.com/b/um2aoetmf9qip/



 def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
    
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
        


# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def isBalanced(self, root):
        memo = {}
        return self.isBalancedHelper(root, memo)

    def isBalancedHelper(self, root: TreeNode, memo) -> bool:
        if root is None:
            return True

        if abs(self.tree_height(root.left, memo) - self.tree_height(root.right, memo)) > 1:
            return False
        
        left_is_bal = self.isBalancedHelper(root.left, memo)
        right_is_bal = self.isBalancedHelper(root.right, memo)
        return left_is_bal and right_is_bal
    
    def tree_height(self, root, memo):
        key = id(root)

        if key in memo:
            return memo[key]
        if root is None:
            return -1
    
        left = 1 + self.tree_height(root.left, memo)
        right = 1 + self.tree_height(root.right, memo)

        memo[key] = max(left, right)
        return memo[key]

        # https://leetcode.com/prboblems/n-ary-tree-preorder-traversal/

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        output = [root.val]
        for child in root.children:
            output += self.preorder(child)
        
        return output

    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        output = [root.val]
        for child in root.children:
            output += self.preorder(child)
        
        return output