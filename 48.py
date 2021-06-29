# https://leetcode.com/problems/combinations/
# https://leetcode.com/problems/path-with-maximum-gold/


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxVal = float('-inf')
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                output = self.dfsTraverse(grid, row, col)
                if output > maxVal:
                    maxVal = output
        return maxVal
        
    def dfsTraverse(self, grid, row, col):
        if row < 0 or row > len(grid) - 1:
            return 0

        if col < 0 or col > len(grid[0]) - 1:
            return 0

        if grid[row][col] == 0:
            return 0

        curr = grid[row][col]

        grid[row][col] = 0 # down the stack

        up = self.dfsTraverse(grid, row - 1, col)
        down = self.dfsTraverse(grid, row + 1, col)
        left = self.dfsTraverse(grid, row, col - 1)
        right = self.dfsTraverse(grid, row, col + 1)

        grid[row][col] = curr # up the stack


        maxVal = max(up, down, left, right)
        return curr + maxVal
        #   U
        # L X R 
        #   D