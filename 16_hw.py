class Solution:
    def integerBreak(self, n):
        memo = {}
        return self.integerBreakHelper(n, True, memo)
    
    def integerBreakHelper(self, n, isRoot, memo):
        if (n, isRoot) in memo:
            return memo[(n, isRoot)]

        if n == 0:
            return 1
        
        max_product = float('-inf')
        i = 1
        limit = n - 1 if isRoot else n
        while i <= limit:            
            curr_product = i * self.integerBreakHelper(n - i, False, memo)
            if curr_product > max_product:
                max_product = curr_product
            i += 1
        
        memo[(n, isRoot)] = max_product
        return max_product

# test = Solution()
# print(test.integerBreak(4)) # (2 + 2) -> 

# https://awwapp.com/b/uixzykc4gmpdm/

# time 3^n
# def foo(n):
#     if n <= 0:
#         return
    
#     foo(n - 1)
#     foo(n - 1)
#     foo(n - 1)

# foo(1000)


def foo(n)
    if n <= 0:
        return

    for i in range(1, n + 1):
        foo(n - i)

foo(1000)