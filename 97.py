# https://coderbyte.com/editor/Longest%20Matrix%20Path:Python3

def LongestMatrixPath(strArr):
  max_path = 0
  memo = {}

  for row in range(len(strArr)):
    for col in range(len(strArr[0])):
      curr_path = df_traversal(strArr, row, col, memo)
      if curr_path > max_path:
        max_path = curr_path

  return max_path

def df_traversal(strArr, row, col, memo, last_num = None):
  row_inbounds = 0 <= row < len(strArr)
  col_inbounds = 0 <= col < len(strArr[0])

  if not row_inbounds or not col_inbounds:
    return -1

  curr_num = int(strArr[row][col])

  # important that this comes BEFORE we check the memo, because if the curr_number 
  # is GREATER than the last then, we should NOT check its memoized value
  if last_num is not None:
    if last_num >= curr_num:
      return -1

  if (row, col) in memo:
    return memo[(row, col)]

  deltas = [(0,1), (0,-1), (1,0), (-1,0)]

  max_path = 0
  for row_add, col_add in deltas:
    amount = df_traversal(strArr, row + row_add, col + col_add, memo, curr_num)
    if amount > max_path:
      max_path = amount

  memo[(row, col)] = 1 + max_path

  return memo[(row, col)]

# keep this function call here 
print(LongestMatrixPath(input()))


# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x2, y2 = (0, 0)
        heap = []

        for x1, y1 in points:
            distance = -(math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 ))
            heapq.heappush(heap, (distance, [x1, y1]))
            if len(heap) > k:
                heapq.heappop(heap)

        output = []
        for _ in range(k):
            distance, coordinates = heapq.heappop(heap)
            output.append(coordinates)
        
        return output

# https://leetcode.com/problems/k-closest-points-to-origin/discuss/217999/JavaC%2B%2BPython-O(N)

    #  2      1
# [[1,3],[-2,2]]
# (0, 0)
# distance = √(x1 - x2)^2 + (y1 - y2)^2)
# find smallest k distances
# heap
# keep heap size k
# if minimum > curr_distance:
    # 

# n = # of points
# k = k
# time : O(n * log(k))
# space : O(k)
# (45, [1,3])

# max, k=3
# [5,2,7,19]

# MAXHEAP # [5, 2, 7]

# # output = []

# heap: 5, 2, 7, 19

# DONT DO MANUAL COMPARISONS
# with K trick:
# n log k
# MAX HEAP = minimum k elements
 
#  https://leetcode.com/discuss/interview-question/1235202/Amazon-or-Onsite-or-Determine-Path

https://leetcode.com/problems/robot-bounded-in-circle/

- - - |
  |   |       ->>>>>>>
  | - |


# UDG

(0,1)

# Direction = S
# G

# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.