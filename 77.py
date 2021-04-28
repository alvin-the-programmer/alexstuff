from typing import List

class Solution:
  # c(5, 3)
  # -> c(4, 2) (add 5 to each of those)
  # -> c(4, 3)


  def combine(self, n: int, k: int) -> List[List[int]]:
    if n < k:
      return []
    if n == 0 or k == 0:
      return [ [] ]

    with_n = []
    for comb in self.combine(n - 1, k - 1):
      with_n.append([ n, *comb ])

    without_n = self.combine(n - 1, k)
    return with_n + without_n


s = Solution()
print(s.combine(4,2))
# print(s.combine(2,1))


      #       (2,1)  
      #    /        \ 
      # (1,0)       (1,1)
        
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# Input: n = 1, k = 1
# Output: [[1]]


# [
#   [5, 2,4],
#   [5, 3,4],
#   [5, 2,3],
#   [5, 1,2],
#   [5, 1,3],
#   [5, 1,4],
# ]

# https://leetcode.com/problems/shortest-bridge/

# graph
# MINIMUM DISTANCE ALWAYS: breadth first

[[1,A,A],
 [2,1,1],
 [0,0,2]]

 visited1 = [(0, 1, 0), (0, 2, 0), ]
 visited2 = [(2, 2)]

 [[1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,1,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1]]

  # https://leetcode.com/problems/shortest-path-to-get-food/