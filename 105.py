def island_areas(grid):
    visited = set()
    areas = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            curr_area = find_area(grid, row, col, visited)
            if curr_area > 0:
                areas.append(curr_area)
    return areas

def find_area(grid, row, col, visited):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return 0

    if grid[row][col] == 0:
        return 0

    if (row,col) in visited:
        return 0

    visited.add((row, col))

    deltas = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    curr_area = 1
    for row_add, col_add in deltas:
        # curr_row 
        new_row = (row + row_add) % len(grid) if (row + row_add) > -1 else len(grid) - 1
        new_col = (col + col_add) % len(grid[0]) if (col + col_add) > -1 else len(grid) - 1

        curr_area += find_area(grid, new_row, new_col, visited)

    return curr_area

grid = [
    [1,0,1,0,0,0,0,1,0,0,0,0,0], 
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,1] 
                #    (n-1, col)
]
print(island_areas(grid)) # [1, 4, 5, 15, 2]



https://leetcode.com/problems/shortest-bridge/
