# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        memo = {}
        return self.findPathsHelper(m, n, N, i, j, memo) % (10**9 + 7)
        
    def findPathsHelper(self, m, n, N, i, j, memo):
        key = (i, j, N)
    
        if key in memo:
            return memo[key]
        if N < 0:
            return 0
        if i < 0 or i > m - 1 or j < 0 or j > n - 1:
            return 1
       
        top = self.findPathsHelper(m, n, N - 1, i - 1, j, memo)
        bottom = self.findPathsHelper(m, n, N - 1, i + 1, j, memo)
        left = self.findPathsHelper(m, n, N - 1, i, j - 1, memo)
        right = self.findPathsHelper(m, n, N - 1, i, j + 1, memo)
        
        memo[key] = top + bottom + left + right
        return memo[key]
# TIME:
# O(4^N)
# after memo: O(Nmn)

# SPACE:
# O(Nmn) for call stack
# N bc height of tree never goes beyond N length
# Nmn bc we create a "memo" object with N*m*n possibilities

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         arrayOfNodes = self.traverse(root)
        
#         for idx in range(len(arrayOfNodes)):
#             arrayOfNodes[idx].left = None
#             if idx == len(arrayOfNodes) - 1:
#                 arrayOfNodes[idx].right = None
#             else:
#                 arrayOfNodes[idx].right = arrayOfNodes[idx + 1]
        
#     def traverse(self, root):
#         if root == None:
#             return []
        
#         return [root] + self.traverse(root.left) + self.traverse(root.right)



class Solution:
    def flatten(self, root: TreeNode) -> None:
        arrayOfNodes = []
        self.traverse(root, arrayOfNodes)
        
        for idx in range(len(arrayOfNodes)):
            arrayOfNodes[idx].left = None
            if idx == len(arrayOfNodes) - 1:
                arrayOfNodes[idx].right = None
            else:
                arrayOfNodes[idx].right = arrayOfNodes[idx + 1]
        
    def traverse(self, root, arrayOfNodes):
        if root is None:
            return
        
        arrayOfNodes.append(root)

        self.traverse(root.left, arrayOfNodes)
        self.traverse(root.right, arrayOfNodes)


# TIME
# n = number of nodes in the tree
# O(n)
# SPACE
# O(n)

# https://awwapp.com/b/uy0bvbyhl0oad/