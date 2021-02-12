# https://awwapp.com/b/unnpzryixngad/#

# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatchHelper(s, p)
        
    def isMatchHelper(self, s, p):
        if not s and not p:
            return True
        if s and not p:
            return False

        # if not s and p[0] != '*':
        #     return False
        
        if not s or not p:
            return False

        

        if p[0] == '*':
            if self.isMatchHelper(s[1:], p[1:]):
              return True

            if s and self.isMatchHelper(s[1:], p):
              return True
            
        if s[0] == p[0] or p[0] == '?':
            return self.isMatchHelper(s[1:], p[1:])

        return False

test = Solution()
print(test.isMatch("boot", "?oot"))# T
print(test.isMatch("boot", "?o?t"))# T
print(test.isMatch("boot", "?ot")) # F
print(test.isMatch("boot", "?sdsdst"))# F

print(test.isMatch("bsddast", "*sdsdst"))# F
print(test.isMatch("boot", "b**t"))# T
print(test.isMatch("apple", "*"))# T
print(test.isMatch("apple", "apple*"))# T
print(test.isMatch("x", "*"))# T
print(test.isMatch("", "*"))# T
print(test.isMatch("", "*s"))# F

