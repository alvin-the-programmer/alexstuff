# flatten bt 
# pascals iteratively
# 1d candy crush "aaabbbc"


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
          return [[1]]

        pre_output = self.generate(numRows - 1)
        curr_row = []
        
        for i in range(numRows):
          if i == 0 or i == (numRows - 1):
            curr_row.append(1)
          else:
            # [1,1]
            last_row = pre_output[-1]
            curr_row.append(last_row[i - 1] + last_row[i])

        pre_output.append(curr_row)
        return pre_output