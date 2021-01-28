# https://leetcode.com/problems/dungeon-game/
# https://awwapp.com/b/ur10fbckgd6d7/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        memo = {}
        return self.calculateMinimumHPHelper(dungeon, 0, 0, memo)
    
    def calculateMinimumHPHelper(self, dungeon, row, col, memo):
        key = (row, col)
        if key in memo:
            return memo[key]

        if row > len(dungeon) - 1 or col > len(dungeon[0]) - 1:
            return float('inf')

        if row == len(dungeon) - 1 and col == len(dungeon[0]) - 1:
            return max(-dungeon[row][col], 0) + 1
        
        right = -dungeon[row][col] + self.calculateMinimumHPHelper(dungeon, row, col + 1, memo)
        if right <= 0:
            right = 1
    
        down = -dungeon[row][col] + self.calculateMinimumHPHelper(dungeon, row + 1, col, memo)
        if down <= 0:
            down = 1

        memo[key] = min(right, down)
        return memo[key]