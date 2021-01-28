class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.longestCommonSubsequenceHelper(text1, text2, 0, 0, memo)

    def longestCommonSubsequenceHelper(self, text1, text2, idx_1, idx_2, memo):
        key = (idx_1, idx_2)
        if key in memo:
            return memo[key]
        
        if len(text1) == idx_1 or len(text2) == idx_2:
            return 0
        if text1[idx_1] == text2[idx_2]:
            left = 1 + self.longestCommonSubsequenceHelper(text1, text2, idx_1 + 1, idx_2 + 1, memo)
            right = float('-inf')
        else:
            left = self.longestCommonSubsequenceHelper(text1,  text2, idx_1 + 1, idx_2, memo)
            right = self.longestCommonSubsequenceHelper(text1,  text2, idx_1, idx_2 + 1, memo)
        
        memo[key] = max(left, right)
        return memo[key]