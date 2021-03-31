# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        return self.findTargetSumWaysHelper(nums, 0, S, memo)

    def findTargetSumWaysHelper(self, nums, idx, S, memo):
        key = (idx, S)
        if key in memo:
            return memo[key]

        if idx == len(nums):
            if S == 0:
                return 1
            else:
                return 0
        left = self.findTargetSumWaysHelper(nums, idx + 1, S - nums[idx], memo)
        right = self.findTargetSumWaysHelper(nums, idx + 1, S + nums[idx], memo)

        memo[key] = left + right
        return memo[key]