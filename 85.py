# https://leetcode.com/problems/meeting-rooms/
# https://leetcode.com/problems/meeting-rooms/

# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# [[0,30],[5,10],[15,20]]

# Output: false

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# [[2,4] [7,10]]

# Output: true

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
      intervals.sort(key = lambda interval: interval[0])
  
      for idx in range(len(intervals) - 1):
        _, curr_int_end = intervals[idx]
        next_int_st, _ = intervals[idx + 1]

        if curr_int_end > next_int_st:
          return False

      return True

# https://leetcode.com/problems/meeting-rooms-ii/

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      intervals.sort(key = lambda interval: interval[0])
      heap = [] 
      # heapq.heappush(heap, item)
      # heapq.heappop(heap)
      for interval in intervals:
        start, end = interval
        
        if heap and start >= heap[0]:
          heapq.heappop(heap)
        heapq.heappush(heap, end)
      
      return len(heap)

        
# [[1,5], [1,5], [1,5], [1,5], [6,8], [6,8]]
                                        X

      #  [5,5,8,8]

# intervals = [[0,30],[5,10],[15,20], ..............]
#                               .     
              # 30

              # 20
              #  \
              #  30



              # 10
            #  / \
          #  20  30



# https://leetcode.com/problems/coin-change/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
# Example 4:

# Input: coins = [1], amount = 1
# Output: 1
# Example 5:

# Input: coins = [1], amount = 2
# Output: 2

# table = 
# []
"""
 table[i]  [0 1 1 2 2 1 2 2          ]
 i:         0 1 2 3 4 5 6 7 8 9 10 11   
"""        

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      table = [None] * (amount + 1)
      table[0] = 0

      for idx, min_coins in enumerate(table):
        for coin in coins:
          if min_coins is not None:
            new_amt = idx + coin
            if new_amt < len(table):
              if table[new_amt] is None or (min_coins + 1) < table[new_amt]:
                table[new_amt] = min_coins + 1
      return -1 if table[-1] is None else table[-1]

multilinear:
 nm
 n + m
#  n^m
#  n^3
