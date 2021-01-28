# https://leetcode.com/problems/unique-paths-ii/
# https://awwapp.com/b/u80ge3uwtakmf/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        return self.uniquePathsWithObstaclesHelper(obstacleGrid, 0, 0, memo)

    def uniquePathsWithObstaclesHelper(self, obstacleGrid, r, c, memo):
        if (r,c) in memo:
            return memo[(r,c)]
        if r > len(obstacleGrid) - 1 or c > len(obstacleGrid[0]) - 1:
            return 0
        if obstacleGrid[r][c] == 1:
            return 0
        if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
            return 1
        
        numPaths = self.uniquePathsWithObstaclesHelper(obstacleGrid, r + 1, c, memo) + self.uniquePathsWithObstaclesHelper(obstacleGrid, r, c + 1, memo)
        memo[(r,c)] = numPaths
        return numPaths

# https://leetcode.com/problems/integer-break/