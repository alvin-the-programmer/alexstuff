# https: // leetcode.com/problems/unique-paths-ii/
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]], r=0, c=0, memo={}) -> int:
        key = (r, c)
        if key in memo:
            return memo[key]

        row_inbounds = 0 <= r < len(obstacleGrid)
        col_inbounds = 0 <= c < len(obstacleGrid[0])
        inbounds = row_inbounds and col_inbounds

        if (not inbounds) or obstacleGrid[r][c] == 1:
            return 0

        if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
            return 1

        memo[key] = self.uniquePathsWithObstacles(
            obstacleGrid, r + 1, c, memo) + self.uniquePathsWithObstacles(obstacleGrid, r, c + 1, memo)
        return memo[key]


s = Solution()
ans1 = s.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
print(ans1)

ans2 = s.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])
print(ans2)
