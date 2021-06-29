
def find_min_moves(board, target):
    visited = set()
    return traverse(board, target, 0, 0, visited)


def traverse(board, target, r, c, visited):
    visited.add((r, c))

    if not target:
        return ''

    new_target = target
    if board[r][c] == target[0]:
        new_target = target[1:]
    options = []

    if r - 1 >= 0 and (r - 1, c) not in visited:
        up = 'U' + traverse(board, new_target, r - 1, c, set(visited))
        options.append(up)
    if r + 1 < len(board) and (r + 1, c) not in visited:
        down = 'D' + traverse(board, new_target, r + 1, c, )
        options.append(down)
    if c - 1 >= 0 and (r, c - 1) not in visited:
        left = 'L' + traverse(board, new_target, r, c - 1)
        options.append(left)
    if c + 1 < len(board[r]) and (r, c + 1) not in visited:
        right = 'R' + traverse(board, new_target, r, c + 1)
        options.append(right)

    min_length_word = options[0]

    for curr_word in options:
        if len(curr_word) < len(min_length_word):
            min_length_word = curr_word

    if new_target != target:
        return '!' + min_length_word
    return min_length_word


# board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
# target = 'leet'
# find_min_moves(board, target)
