# https://leetcode.com/problems/combination-sum-iv/submissions/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.combinationSum4Helper(nums, target, memo)
    
    def combinationSum4Helper(self, nums, target, memo):
        if target in memo:
            return memo[target]
        
        if target == 0:
            return 1
        
        if target < 0:
            return 0
        
        total = 0
        for num in nums:
            total += self.combinationSum4Helper(nums, target - num, memo)
        
        memo[target] = total
        return memo[target]