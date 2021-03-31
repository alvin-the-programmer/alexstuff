def grid_traveler(m, n):
    table = []
    for _ in range(m + 1):
        row = []
        for _ in range(n + 1):
            row.append(0)
        table.append(row)

    table[1][1] = 1

    for i in range(len(table)):
        for j in range(len(table[0])):
            curr = table[i][j]

            if i + 1 < len(table):
                table[i + 1][j] += curr
            if j + 1 < len(table[0]):
                table[i][j + 1] += curr

    return table[m][n]


def can_sum(target, nums):
    table = [None] * (target + 1)
    table[0] = True

    return table[target]


# print(grid_traveler(3, 3))
# print(grid_traveler(18, 18))


print(can_sum(7, [3, 2, 4, 1]))  # true
