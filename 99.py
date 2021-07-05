# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = deque([])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr = grid[row][col]
                if curr == 1:
                    fresh.add((row, col))
                elif curr == 2:
                    rotten.append((row, col, 0))
        
        max_minutes = self.bf_traversal(grid, fresh, rotten)

        if fresh:
            return -1
        
        return max_minutes

    def bf_traversal(self, grid, fresh, rotten):
        minutes = 0
        while rotten:
            row, col, minutes = rotten.popleft()

            deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for row_add, col_add in deltas:
                neighbor = (row + row_add, col + col_add)
                if neighbor in fresh:
                    fresh.remove(neighbor)
                    rotten.append((*neighbor, minutes + 1))

        return minutes



# XOOO
# XOOO
# XOOO
# XXXX

# 3


# Breadth first search in a edged UNWEIGHTED graph will find the shortest path between two points
# as the first path explored between the two points


#    1
# A ---- B
# |
# | 3
# |
# C



class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        memo = {}
        min_diff = self.minDifficultyHelper(jobDifficulty, d, 0, memo)

        if min_diff == float('inf'):
            return -1
        return min_diff

    def minDifficultyHelper(self, jobDifficulty, d, idx, memo):
        key = (d, idx)

        if key in memo:
            return memo[key]

        if idx >= len(jobDifficulty) and d > 0:
            return float('inf')

        if d == 0 and idx < len(jobDifficulty):
            return float('inf')

        if d == 0 and idx >= len(jobDifficulty):
            return 0

        min_diff = float('inf')
        curr_max = jobDifficulty[idx] # TODO
        
        for i in range(idx + 1, len(jobDifficulty) + 1):
            curr_diff = curr_max + self.minDifficultyHelper(jobDifficulty, d - 1, i, memo)
            if curr_diff < min_diff:
                min_diff = curr_diff
            if i < (len(jobDifficulty)) and jobDifficulty[i] > curr_max:
                curr_max = jobDifficulty[i]
                
        memo[key] = min_diff
        return memo[key]



# [a, b, c ] d = 1


# [1 2 3] , d = 2

# 4
# [3
# 2]       [1]
        

# 5
# [3      [2
# ]       1]

#             4
            
#             5 [3, 2, 1], 4              inf                 d = 2

#                [3] /   \ [3, 2]        \ [3,2,1]            

#       inf[2,1]2         [1]  1           []  inf        d = 1      
                            
#     [2]  /   \ [2,1]       \ [1] 1  
          
#    inf [1]     [] 0          [] 0                       d =0



#    d1: [3, 2] = diff 3 
#    d2: [1]    = diff 1
#                 ______
#                      4