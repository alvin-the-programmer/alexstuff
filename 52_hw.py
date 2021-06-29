# https://leetcode.com/problems/counting-bits/solution/
from collections import deque


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]*(num+1)
        for i in range(1, num+1):
            result[i] = result[i & (i-1)] + 1
        return result

# 10    2   1
# 11    3   2
# 2 & 3 = 2 BECAUSE:

# 10
# 11 & =
# 10

# https://leetcode.com/problems/as-far-from-land-as-possible


class Solution:
    def maxDistance(self, grid):
        maxD = -1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    output = self.bfsGrid(grid, row, col)
                    if output > maxD:
                        maxD = output
        if maxD == float('inf'):
            return -1
        else:
            return maxD

    def bfsGrid(self, grid, r, c):
        queue = deque([(r, c, 0)])

        visited = set()
        while queue:
            r, c, layer = queue.popleft()
            visited.add((r, c))
            if grid[r][c] == 1:
                return layer
            else:
                if r - 1 >= 0 and (r-1, c) not in visited:
                    queue.append((r-1, c, layer + 1))
                if r + 1 < len(grid) and (r+1, c) not in visited:
                    queue.append((r+1, c, layer + 1))
                if c - 1 >= 0 and (r, c-1) not in visited:
                    queue.append((r, c - 1, layer + 1))
                if c + 1 < len(grid[0]) and (r, c+1) not in visited:
                    queue.append((r, c + 1, layer + 1))

        return float('inf')

# https://leetcode.com/problems/house-robber-ii/submissions/


def maxDistance(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
    if len(q) == m * n or len(q) == 0:
        return -1
    level = 0
    while q:
        size = len(q)
        for _ in range(size):
            i, j = q.popleft()
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xi, yj = x+i, y+j
                if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                    q.append((xi, yj))
                    grid[xi][yj] = 1
        level += 1
    return level-1

    # 1 0 0     q: (0,2)    size: 1
    # 1 0 0     level: 2
    # 1 1 1


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.robHelper(nums, 0, memo)

    def robHelper(self, nums, i, memo, pickedFirst=False):
        key = (pickedFirst, i)

        if key in memo:
            return memo[key]

        # out of bounds
        if i >= len(nums):
            return 0

        # on the entire subtree where we picked the first number, don't pick the last item
        if i == len(nums) - 1 and pickedFirst == True:
            return 0

        # pick
        if i == 0:
            left = nums[i] + self.robHelper(nums, i + 2, memo, True)
        else:
            left = nums[i] + self.robHelper(nums, i + 2, memo, pickedFirst)

        # don't pick
        right = self.robHelper(nums, i + 1, memo, pickedFirst)

        memo[key] = max(left, right)
        return memo[key]
