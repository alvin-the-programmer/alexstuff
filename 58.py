# https://leetcode.com/problems/minimum-cost-for-tickets/

# https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int, mod=10 ** 9 + 7) -> int:
        # arr *= k
        def Kadane(arr, res=0, cur=0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res

        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod if k > 1 else Kadane(arr) % mod


It took me a while to understand how there isn't a bug in here - at first glance, it looks like some of the cases are not covered.

For anyone else struggling, consider that:

Kadane(arr * 2) is always >= Kadane(arr)
Kadane(arr * 2) will always cross the boundary if sum(arr) > 0
if Kadane(arr * 2) does not cross the boundary, then Kadane(arr * 2) == Kadane(arr)
