# https://leetcode.com/problems/unique-binary-search-trees-ii/

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        memo = {}
        return self.generateTreesHelper(1, n, memo)
    
    def generateTreesHelper(self, low, upp, memo): # [1, 3]
        key = (low, upp)

        if key in memo:
            return memo[key]
        if low > upp:
            return [None]
        
        all_trees = []
        
        # i = 1 ## i = 2 ### i = 3
        for i in range(low, upp + 1): # [1, 4] 
            left_trees = self.generateTreesHelper(low, i - 1, memo) # (1, 0) = [None]             ## (1, 1) = [[1]]   ### (1, 2) = [[1, 2], [2, 1]]
            right_trees = self.generateTreesHelper(i + 1, upp, memo) # (2, 3) = [[2,3], [3,2]]    ## (3, 3) = [[3]]   ### (4, 3) = [None]
            
            for j in left_trees:
                for k in right_trees:
                    curr_tree = TreeNode(i)
                    curr_tree.left = j
                    curr_tree.right = k
                    all_trees.append(curr_tree)
        memo[key] = all_trees
        return memo[key]


# https://awwapp.com/b/uyqzxzkmsb2hx/