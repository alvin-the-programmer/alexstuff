class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.messages:
            if timestamp < (self.messages[message] + 10):
                return False
        self.messages[message] = timestamp
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


#  solution i stumbled across somehow but after drawing it out, i have no idea how this works
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        scores = self.stoneGameHelper(piles, 0, len(piles) - 1, memo)
        
        return True if scores[0] >= scores[1] else False
    
    def stoneGameHelper(self, piles, front_idx, back_idx, memo):
        key = (front_idx, back_idx)
        if key in memo:
            return memo[key]
        
        if front_idx == back_idx:
            return [0, 0]
        
        front = self.stoneGameHelper(piles, front_idx + 1, back_idx, memo)
        back = self.stoneGameHelper(piles, front_idx, back_idx - 1, memo)
            
        memo[key] = [max(front[0], back[0]), max(front[1], back[1])]
        return memo[key]




class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        scores = self.stoneGameHelper(piles, 0, len(piles) - 1, True, memo)
        return True if scores[0] > scores[1] else False
    
    def stoneGameHelper(self, piles, front_idx, back_idx, player, memo):
        key = (front_idx, back_idx, player)

        if key in memo:
            return memo[key]

        if front_idx >= back_idx:
            return [0,0]
        
        front = self.stoneGameHelper(piles, front_idx + 1, back_idx, not player, memo)
        front_move = piles[front_idx]

        back = self.stoneGameHelper(piles, front_idx, back_idx - 1, not player, memo)
        back_move = piles[back_idx]

        options = []

        if player == True:
            options.append([front[0] + front_move, front[1]])
            options.append([back[0] + back_move, back[1]])
        else:
            options.append([front[0], front[1] + front_move])
            options.append([back[0], back[1] + back_move])
        
        if player == True:
            if options[0][0] > options[1][0]:
                memo[key] = options[0]
                return memo[key]
        else:
            if options[0][1] > options[1][1]:
                memo[key] = options[0]
                return memo[key]
            
        memo[key] = options[1]
        return memo[key]
        
        # if player == True:
        #     max(front[0], back[0])
        #     return [next_call[0] + curr_move, next_call[1]]
        # else:
        #     return [next_call[0], next_call[1] + curr_move]

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        alex = take(piles, 0, len(piles) - 1, {})
        lee = total - alex
        return alex > lee
        
def take(arr, i, j, memo):
    key = (i, j)
    if key in memo:
        return memo[key]
    
    if i > j:
        return 0
    
    memo[key] = max(
        arr[i] + take(arr, i + 2, j, memo), # a takes front, l takes front
        arr[i] + take(arr, i + 1, j - 1, memo),
        arr[j] + take(arr, i, j - 2, memo),
        arr[j] + take(arr, i + 1, j - 1, memo)
    )

# 4^(n / 2)  == 




# 2^(n) 



# 2^3 x 2^4 = 2^7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# class Solution:
#     def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
#         queue_1 = deque([root1, 0])
#         queue_2 = deque([root2, 0])
        
#         set_1 = set([root1.val])
#         set_2 = set([root2.val])
        
#         curr_level = 0
        
#         while queue_1 or queue_2:
#             first_root = queue_1.popleft()
#             second_root = queue_2.popleft()



class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False
        
        left = self.flipEquiv(root1.left, root2.left)
        right = self.flipEquiv(root1.right, root2.right)
        no_flip = left and right

        left_flip = self.flipEquiv(root1.right, root2.left)
        right_flip = self.flipEquiv(root1.left, root2.right)
        use_flip = left_flip and right_flip

        return no_flip or use_flip

class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))

# [1 2 3 4     5 6 None None 7    8  None]
# [1 3 2 None  6 4 5    None None 8  7]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float('-inf')
        curr_max = float('-inf')
        
        for num in nums:
            curr_max = max(num, num + curr_max)
            if curr_max > global_max:
                global_max = curr_max
        return global_max

    # TO DOS
    # https://leetcode.com/problems/same-tree/
    # https://leetcode.com/problems/symmetric-tree/
    # https://leetcode.com/problems/invert-binary-tree/