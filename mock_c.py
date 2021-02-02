# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        return self.minPathSumHelper(grid, 0, 0, memo)

    def minPathSumHelper(self, grid, r, c, memo):
        key = (r, c)
        if key in memo:
            return memo[key]

        if r >= len(grid) or c >= len(grid[0]):
            return float('inf')

        curr = grid[r][c]
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return curr
        
        down = curr + self.minPathSumHelper(grid, r + 1, c, memo)
        right = curr + self.minPathSumHelper(grid, r, c + 1, memo)

        memo[key] = min(down, right)
        return memo[key]

https://leetcode.com/problems/longest-string-chain/