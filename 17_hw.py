from typing import List

# https://leetcode.com/problems/paint-house-ii/
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        memo = {}
        return self.minCostHelper(0, None, costs, memo)

    def minCostHelper(self, houseNum, lastColor, costs, memo):
        key = (houseNum, lastColor)
        if key in memo:
            return memo[key]

        if houseNum > len(costs) - 1:
            return 0
        
        minimum = float('inf')
        for i in range(0, len(costs[0])):
            color_cost = costs[houseNum][i] + self.minCostHelper(houseNum + 1, i, costs, memo)
            if i != lastColor and color_cost < minimum:
                minimum = color_cost
        
        memo[key] = minimum
        return memo[key]

# https://leetcode.com/problems/house-robber/

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         memo = {}
#         return self.robHelper(nums, memo)
        
#     def robHelper(self, nums, memo):
#         key = tuple(nums)
#         if key in memo:
#             return memo[key]
        
#         if nums == []:
#             return 0
        
#         maximum = float('-inf')
#         for i in range(len(nums)):
#             curr = nums[i] + self.robHelper(nums[i+2:], memo)
#             if curr > maximum:
#                 maximum = curr
#         memo[key] = maximum
#         return maximum

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.robHelper(nums, memo, 0)
        
    def robHelper(self, nums, memo, i):
        key = i
        if key in memo:
            return memo[key]

        if i >= len(nums):
            return 0
        
        left = self.robHelper(nums, memo, i + 1)
        right = nums[i] + self.robHelper(nums, memo, i + 2)

        memo[key] = max(left, right)
        return memo[key]

# https://awwapp.com/b/ugqwisntosnet/asdasd



# def sum_array(nums, i = 0):
#     if i == len(nums):
#         return 0;

#     return nums[i] + sum_array(nums, i + 1)


# def sum_array(nums, total = 0):
#     if 0 == len(nums):
#         return total;

#     return sum_array(nums[1:], total + nums[0])


print(sum_array([3,2,1,7]))