class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        for r in range(len(grid)): # O(rc)
            for c in range(len(grid[0])):
                # if (r,c) not in visited:
                if self.explore(grid, r, c, visited) == True:
                    islands += 1
        return islands
    
    def explore(self, grid, r, c, visited):
        if (r,c) in visited:
            return False

        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
            return False

        if grid[r][c] == '0':
            return False

        visited.add((r,c))
        top = self.explore(grid, r - 1,  c, visited)
        bottom = self.explore(grid, r + 1,  c, visited)
        left = self.explore(grid, r,  c - 1, visited)
        right = self.explore(grid, r,  c + 1, visited)
        return True

# space: O(rc) for the set
# space: O()