# https://leetcode.com/problems/counting-bits/solution/
from collections import deque


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]*(num+1)
        for i in range(1, num+1):
            result[i] = result[i & (i-1)] + 1
        return result

# 10    2   1
# 11    3   2
# 2 & 3 = 2 BECAUSE:

# 10
# 11 & =
# 10

# https://leetcode.com/problems/as-far-from-land-as-possible


class Solution:
    def maxDistance(self, grid):
        maxD = -1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    output = self.bfsGrid(grid, row, col)
                    if output > maxD:
                        maxD = output
        if maxD == float('inf'):
            return -1
        else:
            return maxD

    def bfsGrid(self, grid, r, c):
        queue = deque([(r, c, 0)])
        count = 0
        visited = set()
        while queue:
            r, c, layer = queue.popleft()
            visited.add((r, c))
            if grid[r][c] == 1:
                return layer
            else:
                if r - 1 >= 0 and (r-1, c) not in visited:
                    queue.append((r-1, c, layer + 1))
                if r + 1 < len(grid) and (r+1, c) not in visited:
                    queue.append((r+1, c, layer + 1))
                if c - 1 >= 0 and (r, c-1) not in visited:
                    queue.append((r, c - 1, layer + 1))
                if c + 1 < len(grid[0]) and (r, c+1) not in visited:
                    queue.append((r, c + 1, layer + 1))

        return float('inf')
