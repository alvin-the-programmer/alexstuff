class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.longestCommonSubsequenceHelper(text1, text2, memo, 0, 0)
        
    def longestCommonSubsequenceHelper(self, text1, text2, memo, i, j):
        key = (i, j)
        
        if key in memo:
            return memo[key]
        
        if i >= len(text1) and j >= len(text2):
            return 0
        
        if i >= len(text1) or j >= len(text2):
            return 0
        
        if text1[i] == text2[j]:
            memo[key] = 1 + self.longestCommonSubsequenceHelper(text1, text2, memo, i + 1, j + 1)
            return memo[key]
        else:
            left = self.longestCommonSubsequenceHelper(text1, text2, memo, i + 1, j)
            right = self.longestCommonSubsequenceHelper(text1, text2, memo, i, j + 1)
        
        memo[key] = max(left, right)
        return memo[key]

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        return self.longestPalindromSubseqHelper(s, memo)
    
    def longestPalindromSubseqHelper(self, s, memo):
        key = s
        if key in memo:
            return memo[key]
        
        if len(s) == 1:
            return 1

        if not s:
            return 0

        lastChar = len(s) - 1
        if s[0] == s[lastChar]:
            memo[key] = 2 + self.longestPalindromSubseqHelper(s[1:lastChar], memo)
            return memo[key]
        else:
            left = self.longestPalindromSubseqHelper(s[1:], memo)
            right = self.longestPalindromSubseqHelper(s[:lastChar], memo)
            memo[key] = max(left, right)
            return memo[key]
    