# https://awwapp.com/b/uta6pb99j4nar/
# https://leetcode.com/problems/max-area-of-island/
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        master_visited = set()
        
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curr_area = self.maxAreaOfIslandHelper(grid, r, c, master_visited)
                if curr_area > max_area:
                    max_area = curr_area
        return max_area

    def maxAreaOfIslandHelper(self, grid, r, c, master_visited):
        curr = (r, c)
        if curr in master_visited:
            return 0
        row_good = 0 <= r < len(grid)
        col_good = 0 <= c < len(grid[0])
        if not row_good or not col_good:
            return 0
        if grid[r][c] == 0:
            return 0
        if grid[r][c] == 1:
            master_visited.add(curr)
            top = self.maxAreaOfIslandHelper(grid, r - 1, c, master_visited)
            bottom = self.maxAreaOfIslandHelper(grid, r + 1, c, master_visited)
            left = self.maxAreaOfIslandHelper(grid, r, c - 1, master_visited)
            right = self.maxAreaOfIslandHelper(grid, r, c + 1, master_visited)
            return 1 + top + bottom + left + right

g1 = {
    'q' : ['s', 'r'],
    's' : ['t'],
    't' : ['u'],
    'r' : ['t', 'u'],
    'u' : []
}

def get_path(graph, src, dest):
    visited = set()
    return get_path_helper(graph, src, dest, visited)

def get_path_helper(graph, src, dest, visited):
    neighbors = graph[src]
    if src == dest:
        return [src]
    if src in visited:
        return None
    visited.add(src)
    for neighbor in neighbors:
        found = get_path_helper(graph, neighbor, dest, visited)
        if found is not None:
            return [src] + found

    return None

print(get_path(g1, 't', 'q'));

# https://leetcode.com/problems/all-paths-from-source-to-target/