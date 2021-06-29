# https://leetcode.com/problems/majority-element/
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxEle = None
        for ele in freq:
            if maxEle is None or freq[ele] > freq[maxEle]:
                maxEle = ele
        return maxEle

# nums = [2, 2, 2, 2, 2, 4, 3, 5]
# len(nums) = 8
# # maxEle = 2
# freq = {
#     2: 5, # <- 2
#     3: 1,
#     4: 1,
#     5: 1
# }
                
# Boyer Moore Voting Algo
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

# count = 1
# candidate = 2
# nums = [2,2,1,1,1,2,2]
                      
# ceil(n/2)
# 4

# https://docs.google.com/document/d/15LQQ2xvVCxjxLw-8kSRS9wZBkyoOVYhfLYryDky8ECc/edit?usp=sharing