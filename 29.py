# https://awwapp.com/b/unnpzryixngad/#

# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.isMatchHelper(s, p, memo)
        
    def isMatchHelper(self, s, p, memo, i = 0, j = 0):
        key = (i, j)
        if key in memo:
            return memo[key]
        if i == len(s) and j == len(p):
            return True

        if i < len(s) and j == len(p):
            return False
 
        if (i == len(s) or j == len(p)) and p[j] != '*':
            return False

        if p[j] == '*':
            if i == len(s):
                memo[key] = self.isMatchHelper(s, p, memo, i, j + 1)
                return memo[key]
            else:
                memo[key] = self.isMatchHelper(s, p, memo, i + 1, j) or self.isMatchHelper(s, p, memo, i, j + 1)
                return memo[key]
            
        if s[i] == p[j] or p[j] == '?':
            memo[key] = self.isMatchHelper(s, p, memo, i + 1, j + 1)
            return memo[key]

        memo[key] = False
        return False

test = Solution()
print(test.isMatch('aa', 'a')) # F
print(test.isMatch('a', '')) # F

# print(test.isMatch("", "*")) # T

# print(test.isMatch("boot", "?oot"))# T
# print(test.isMatch("boot", "?o?t"))# T
# print(test.isMatch("boot", "?ot")) # F
# print(test.isMatch("boot", "?sdsdst"))# F

# print(test.isMatch("bsddast", "*sdsdst"))# F
# print(test.isMatch("boot", "b**t"))# T
# print(test.isMatch("apple", "*"))# T
# print(test.isMatch("apple", "apple*"))# T
# print(test.isMatch("x", "*"))# T
# print(test.isMatch("", "*"))# T
# print(test.isMatch("", "*s"))# F

# https://awwapp.com/b/uwyrr2syjyjln/

