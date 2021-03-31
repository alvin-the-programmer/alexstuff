def is_sub_full(grid):
    output = []
    all_nums = set([1, 2, 3, 4])
    curr_col = 0
    while len(output) < len(grid[0]) - 1:
        top_left = grid[0][curr_col]
        top_right = grid[0][curr_col + 1]
        bottom_left = grid[1][curr_col]
        bottom_right = grid[1][curr_col + 1]
        curr_nums = set([top_left, top_right, bottom_left, bottom_right])

        if curr_nums == all_nums:
            output.append(True)
        else:
            output.append(False)
        curr_col += 1

    return output


grid = [[1, 3, 1], [2, 4, 3]]
print(is_sub_full(grid))
