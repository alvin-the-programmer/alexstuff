from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
      crushed = True
      while crushed:
        crushed = False
        if self.play_round(board) == True:
          crushed = True
        self.push_zeroes_up(board)

    def push_zeroes_up(self, board):
        for col in range(len(board[0])):
            stored_values = []
            for row in range(len(board)):
                curr_candy = board[row][col]
                if curr_candy != 0:
                    stored_values.append(curr_candy)

            num_of_zeroes = len(board) - len(stored_values)
            for row in range(num_of_zeroes):
                board[row][col] = 0

            for row in range(num_of_zeroes, len(board)):
                board[row][col] = stored_values[row - num_of_zeroes]

        return board

    def play_round(self, board):
        positions_to_change = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                crushed_vertical_positions = self.crush_vertical(
                    board, row, col, board[row][col])
                crushed_horizontal_positions = self.crush_horizontal(
                    board, row, col, board[row][col])

                if len(crushed_vertical_positions) > 2:
                    positions_to_change += crushed_vertical_positions
                    
                if len(crushed_horizontal_positions) > 2:
                    positions_to_change += crushed_horizontal_positions
                    
        self.change_to_zero(board, positions_to_change)
        
        if len(positions_to_change) > 2:
          return True
        return False

    def crush_vertical(self, board, row, col, first_candy):
        # out of bounds or if we hit a candy that isnt the same
        if first_candy == 0:
            return []

        is_row_inbounds = 0 <= row < len(board)

        if not is_row_inbounds or board[row][col] != first_candy:
            return []

        output = self.crush_vertical(board, row + 1, col, first_candy)
        output.append((row, col))

        return output

    def crush_horizontal(self, board, row, col, first_candy):
        if first_candy == 0:
            return []
        is_col_inbounds = 0 <= col < len(board[0])

        if not is_col_inbounds or board[row][col] != first_candy:
            return []

        output = self.crush_horizontal(board, row, col + 1, first_candy)
        output.append((row, col))

        return output

    def change_to_zero(self, board, positions):
        for position in positions:
            row, col = position
            board[row][col] = 0
        return board


# Candy Crush 1D
# Input: "aaabbbc"
# Output: "c"
# Explanation:
# 1. Remove 3 'a': "aaabbbbc" => "bbbbc"
# 2. Remove 4 'b': "bbbbc" => "c"

def candy_crush_1d(str_to_crush):
  crushed = True
  while crushed:
    crushed = False
    left = 0
    count = 1

    for right in range(1, len(str_to_crush)):

    if str_to_crush[left] == str_to_crush[right]:
      count += 1
      right