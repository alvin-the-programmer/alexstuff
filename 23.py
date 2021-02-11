# # https://leetcode.com/problems/count-servers-that-communicate/

# a b c d e
# 1 0 0 0 0 1
# 0 1 0 0 0 2
# 0 0 0 0 0 3
# 0 0 0 1 0 4
# 0 1 0 0 1 5


# colCount = {
#   a : 1
#   b : 2
#   c : 0
#   d : 1
#   e : 1
# }

# rowCount = {
#   1 : 1
#   2 : 1
#   3 : 0
#   4 : 1
#   5 : 2
# }

# count = 3


# a b c d e
# 1 0 1 1 0 1
# 0 0 0 0 0 2
# 0 0 0 0 0 3
# 0 0 0 0 0 4
# 0 0 0 0 0 5


# colCount = {
#   a : 1
#   b : 0
#   c : 1
#   d : 1
#   e : 0
# }

# rowCount = {
#   1 : 3
#   2 : 0
#   3 : 0
#   4 : 0
#   5 : 0
# }

# count = 3

def countServers(self, grid):
    colCount = {}
    rowCount = {}

    for row in range(len(grid)):
        rowCount[row] = 0
        for col in range(len(grid[0])):
            if col not in colCount:
                colCount[col] = 0
            if grid[row][col] == 1:
                colCount[col] += 1
                rowCount[row] += 1

    serverCount = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                if rowCount[row] > 1 or colCount[col] > 1:
                    serverCount += 1

    return serverCount

# a b c d
# 1 1 0 0 1 
# 0 0 1 0 2 
# 0 0 1 0 3
# 0 0 0 1 4

# row;
# 1: 2
# 2: 1
# 3: 1
# 4: 1

# col:
# a: 1
# b: 1
# c: 2
# d: 1



# https://awwapp.com/b/ux9z2co6mrgwo/

# https://leetcode.com/problems/leaf-similar-trees/
# https://leetcode.com/problems/satisfiability-of-equality-equations/