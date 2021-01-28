# LC 279  https://leetcode.com/problems/perfect-squares/
# https://awwapp.com/b/ujmxit7y1k9v4/
class Solution:
    # def numSquares(self, n: int) -> int:
    #     memo = {}
    #     return self.numSquaresHelper(n, memo)
    
    def numSquaresHelper(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        best = float('inf')
        
        i = 1
        while i**2 <= n:
            result = self.numSquaresHelper(n - i**2, memo)
            if result < best:
                best = result
            i+=1
        memo[n] = 1 + best
        return memo[n]

    def squares_sum(self, n):
        memo = {}
        return self.squares_sum_helper(n, memo)

    def squares_sum_helper(self, n, memo):
        if n in memo:
            return memo[n]

        if n == 0:
            return []
        
        best = None

        i = 1
        while i**2 <= n:
            candidate = self.squares_sum_helper(n - i**2, memo) + [ i**2 ]
            if best is None or len(candidate) < len(best):
                best = candidate
            i+=1
        
        memo[n] = best
        return memo[n]

        
s = Solution()
# print(s.numSquares(6)) # 3


print(s.squares_sum(6)) # [1, 1, 4]
print(s.squares_sum(72)) # [36,36]


