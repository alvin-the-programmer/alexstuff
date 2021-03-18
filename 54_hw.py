class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_max_sum = global_max_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curr_max_sum = max(num, num + curr_max_sum)
            global_max_sum = max(global_max_sum, curr_max_sum)
        return global_max_sum
