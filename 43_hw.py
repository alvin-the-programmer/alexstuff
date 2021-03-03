# https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        openers = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        
        for brack in s:
            if ')]}'.find(brack) >= 0:
                if stack and stack[-1] == openers[brack]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brack)
        
        return True if not stack else False
# n = # of letters in s
# time: O(s)
# space: O(s)

# https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.minimumTotalHelper(0, 0, triangle, memo)
        
    def minimumTotalHelper(self, idx, row, triangle, memo):
        key = (idx, row)
        if key in memo:
            return memo[key]
        
        curr = triangle[row][idx]
        if row == len(triangle) - 1:
            return curr
        
        left = curr + self.minimumTotalHelper(idx, row + 1, triangle, memo)
        right = curr + self.minimumTotalHelper(idx + 1, row + 1, triangle, memo)
        
        memo[key] = left if left < right else right
        return memo[key]

# n = total # of #'s
# r = # of rows in triangle
# before memo:
# time: O(r!)?
# space: O(log n)

# after memo:
# time: O(n)
# space: O(n)
# call stack space? log (n)