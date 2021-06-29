from sys import dont_write_bytecode


class UndergroundSystem:
    def __init__(self):
      self.pending = {}
      self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
      self.pending[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
      starting_station, start_time = self.pending[id]
      
      trip = (starting_station, stationName)
      if trip not in self.trips:
        self.trips[trip] = {
          'total': 0,
          'num_pass': 0
        }

      curr_trip = self.trips[trip]
      curr_trip['total'] += (t - start_time)
      curr_trip['num_pass'] += 1

      del self.pending[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
      curr_trip = self.trips[(startStation, endStation)]

      return curr_trip['total'] / curr_trip['num_pass']

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# pending: {
#   10 : (Leyton, 3)
# }

# del pending[10]

# stations = {
#     (L, W): {total : t, numPass: p },
#     (W, C): {total : t, numPass: p },
# }



# Total Sum -->
# Input: arr1 = [1,2,3,5], arr2 = [1,10,13,11], target = 15
# Output: True ( 5 (from arr1) + 10(from arr2) == 15(target))
# I solved this question and told him both brute force as well as an optimized solution.

def two_sum(arr1, arr2, target): 
  set2 = set(arr2)

  for num in arr1:
    if (target - num) in set2:
      return True
  return False


# https://leetcode.com/problems/valid-anagram/
# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#       return Counter(s) == Counter(t)
      

# https://leetcode.com/problems/binary-tree-level-order-traversal/

# from collections import deque

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#           return []
#         queue = deque([(root, 0)])
#         output = []
#         while queue:
#           node, level = queue.popleft()

#           if len(output) <= level:
#             output.append([])
          
#           output[level].append(node.val)

#           if node.left is not None:
#             queue.append((node.left, level + 1))
#           if node.right is not None:
#             queue.append((node.right, level + 1))

#         return output



# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]


# https://leetcode.com/problems/minimum-path-sum/

# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      memo = {}
      return self.minPathSumHelper(grid, 0, 0, memo)
      
    def minPathSumHelper(self, grid, row, col, memo):
      key = (row, col)

      if key in memo:
        return memo[key]

      row_inbounds = 0 <= row < len(grid)
      col_inbounds = 0 <= col < len(grid[0])

      if not row_inbounds or not col_inbounds:
        return float('inf')

      curr_cell = grid[row][col]

      if row == (len(grid) - 1) and col == (len(grid[0]) - 1):
        return curr_cell

      down = self.minPathSumHelper(grid, row + 1, col, memo)
      right = self.minPathSumHelper(grid, row, col + 1, memo)

      memo[key] = curr_cell + min(down, right)

      return memo[key]

      

# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]


# 1R, 3R, 1R, 1D, 1D
# 1R, 3D, 5R