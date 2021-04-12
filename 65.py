from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set([(0, 0)])
        spiral_order = [matrix[0][0]]
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        direction = 0
        curr = (0, 0)

        while len(visited) < (len(matrix) * len(matrix[0])):
            row, col = curr

            row_add, col_add = directions[direction % 4]

            temp = (row + row_add, col + col_add)

            row_inbounds = 0 <= temp[0] < len(matrix)
            col_inbounds = 0 <= temp[1] < len(matrix[0])

            if row_inbounds and col_inbounds and temp not in visited:
                curr = temp
                row, col = curr
                spiral_order.append(matrix[row][col])
                visited.add(curr)
            else:
                direction += 1

        return spiral_order


# test = Solution()
# print(test.spiralOrder([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [5, 6, 7, 8],
#     [9, 1, 1, 1]
# ]))

# print(test.spiralOrder([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]))


class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        i = 0  # 0
        while i < len(chars):
            curr_letter = chars[i]
            result.append(curr_letter)
            count = 1
            j = i + 1
            while j < len(chars):
                if chars[j] == curr_letter:
                    count += 1
                else:
                    break
                j += 1
            i = j

            if count > 1:
                for ch in str(count):
                    result.append(ch)

        for idx in range(len(result)):
            chars[idx] = result[idx]
        return len(result)


test = Solution()
print(test.compress(["a", "a", "b", "b", "c", "c", "c", "a"]))
