# https://leetcode.com/problems/cut-off-trees-for-golf-event/

# You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
# In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

# You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

# Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

# You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.

"""
[1,2,3,6,5,4]
sort() (mn log mn)

1 1  
[1,2,3,4,5,6] = O( (mn)^2 )
   X

remove(1) : prev = 1
move down: return 0
move right: 
  is curr > prev
"""

# [
#  [1,2,3],
#  [6,5,4],
# ]

# [
#  [1,0,2,3],
#  [6,0,5,4],
#  [7,8,9,10],

# ]

# [[1,2,3],
#  [6,5,4],
# ]


# Input: forest = 
# [[1,2,3],
#  [0,0,4],
#  [7,6,5]]
# Output: 6
# Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.

# Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
# Output: -1
# Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.

# Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
# Output: 6
# Explanation: You can follow the same path as Example 1 to cut off all the trees.
# Note that you can cut off the first tree at (0, 0) before making any steps.
from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
      trees = []
      for row in range(len(forest)):
        for col in range(len(forest[0])):
          curr_tree = forest[row][col]
          if curr_tree != 0:
            trees.append(curr_tree)

      trees.sort()
      
      pos = (0,0)
      total_dist = 0
      for tree in trees:
        row, col = pos
        new_row, new_col, min_dist = self.get_distance(forest, row, col, tree)
        if min_dist == -1:
          return -1
        total_dist += min_dist
        pos = (new_row, new_col)

      return total_dist

    def get_distance(self, forest, row, col, tree):
      queue = deque([(row, col, 0)])
      visited = set([(row, col)])

      while queue:
        curr_row, curr_col, level = queue.popleft()
        curr_pos = forest[curr_row][curr_col]
        if curr_pos == tree:
          return (curr_row, curr_col, level)

        deltas = [(1,0), (-1,0), (0,1), (0,-1)]

        for delta in deltas:
          row_add, col_add = delta
          new_row = curr_row + row_add
          new_col = curr_col + col_add
          
          row_inbounds = 0 <= new_row < len(forest)
          col_inbounds = 0 <= new_col < len(forest[0])

          if row_inbounds and col_inbounds:
            if forest[new_row][new_col] != 0 and (new_row, new_col) not in visited:
              visited.add((new_row, new_col))
              queue.append((new_row, new_col, level + 1))
      return (-1, -1, -1)


# s = Solution()
# print(s.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))



# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solution/





# There are 8 prison cells in a row and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

# You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

# Return the state of the prison after n days (i.e., n such changes described above).


# OCCUPIED
# [1, 0, 1]
# [1, 1, 1]

# [0, 0, 0]
# [0, 1, 0]

# front or end
# 0 [1, 0, 1] 0

# Example 1:

# Input: cells = [0,1,0,1,1,0,0,1], n = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]


# [0,1,1,1,0,0,1,0]
# Example 2:

# Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
# Output: [0,0,1,1,1,1,1,0]
 

# Constraints:

# cells.length == 8
# cells[i] is either 0 or 1.
# 1 <= n <= 109


# OCCUPIED
# [1, 0, 1]
# [1, 1, 1]

# [0, 0, 0]
# [0, 1, 0]

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
      print(cells)
      current_cells = cells[:]
      for i in range(n):
        current_cells = self.next_day(current_cells)
      return current_cells

    def next_day(self, cells): 
      new_cells = cells[:]
      for idx in range(0, len(cells)):
        lo = cells[idx - 1] if (idx - 1) >= 0 else -1
        hi = cells[idx + 1] if (idx + 1) < len(cells) else -1
  
        if lo == hi:
          new_cells[idx] = 1
        else:
          new_cells[idx] = 0
      return new_cells


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self = x
#         self.left = None
#         self.right = None

# # [3 2]

# [3,5,1,6,2,0,8,null,null,7,4]
# # found_q = True

#             10
#          /    \ 
#         3       12 
#       /    \
#      2      4  
#     /
#    5


# [10, 3,2,5]
# [10, 3,4]

# a [5,2,3, 10]
# b [4,  3, 10]
# set(b) = 4, 3, 10
# b.find(5)
# 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      p_path = self.df_trav_path(root, p) 
      q_path = self.df_trav_path(root, q)
      q_nums = set(q_path)

      for num in p_path:
        if num in q_nums:
          return num

        
      
    def df_trav_path(self, root, dest):
      if root is None:
        return None

      if root == dest:
        return [root]

      left_branch = self.df_trav_path(root.left, dest)
      right_branch = self.df_trav_path(root.right, dest)

      if left_branch:
        left_branch.append(root)
        return left_branch
      elif right_branch:
        right_branch.append(root)
        return right_branch
      
      return None

