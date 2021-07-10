# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            
            if curr.val == subRoot.val:
                if self.check_equality(curr, subRoot) == True:
                    return True
                
            if curr.left:
                queue.append(curr.left)
                
            if curr.right:
                queue.append(curr.right)
        
        return False
    
    def check_equality(self, root, subRoot):
        root_queue = deque([(root, 0, -1)])
        subRoot_queue = deque([(subRoot, 0, -1)])
        
        while root_queue or subRoot_queue:
            if not root_queue or not subRoot_queue:
                return False
        
            curr_root, root_level, root_dir = root_queue.popleft()
            curr_subRoot, subRoot_level, subRoot_dir = subRoot_queue.popleft()
            
            if curr_root.val != curr_subRoot.val or root_level != subRoot_level or root_dir != subRoot_dir:
                return False
            
            if curr_root.left:
                root_queue.append((curr_root.left, root_level + 1, 0))
            if curr_root.right:
                root_queue.append((curr_root.right, root_level + 1, 1))
                
            if curr_subRoot.left:
                subRoot_queue.append((curr_subRoot.left, root_level + 1, 0))
            if curr_subRoot.right:
                subRoot_queue.append((curr_subRoot.right, root_level + 1, 1))
        
        return True

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and subRoot:
            return False
        
        if self.same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def same(self, rootA, rootB):
        if not rootA and not rootB:
            return True
        
        if not rootA and rootB:
            return False
        
        if rootA and not rootB:
            return False
        
        if rootA.val != rootB.val:
            return False
        
        return self.same(rootA.left, rootB.left) and self.same(rootA.right, rootB.right)

        
# a                      a

# a                      a
#                        .
# a                      z

# a

# a

# a


# # https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)


# https://leetcode.com/problems/group-anagrams/


from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        
        groups = []

        for sorted_word in anagrams:
            groups.append(anagrams[sorted_word])

        return groups

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            anagram = ''.join(sorted(s)) 
            groups[anagram].append(s)
            
        return [ group for group in groups.values() ]        
            
# n = # of strs
# x = longest word in strs

# time: O(n(x log x))
# space: O(n)

# in: ['cat', 'tac', 'atc', 'bat']
                    #    x

# {
#    act: [cat, tac, act],
#    abt: [bat]
# }




# out: [['cat', 'tac', 'atc'], ['bat']]

# [act, act, act, abt]

"""
    n = # of words
    x = max length of a word
    O(nx + (n^2)x)
"""

# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3804/


# arr = [3,3,3,3, 5,5,5, 2,2, 7]

# {
#     3: 4
#     5: 3
#     2: 2
#     7: 1
# }

# 10

# min(# of keys) === >= 5


            #            10                          3
            #     4  /        \ 0               
            #       6           10                      5
            #  3  /  \ 0     3 /  \ 0
            #   3      6                                2

from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        value_counts = list(counts.values())
        memo = {}
        return self.minSetSizeHelper(0, value_counts, len(arr), len(arr) // 2, memo)

    def minSetSizeHelper(self, idx, value_counts, length, target_length, memo):
        key = (idx, length)

        if key in memo:
            return memo[key]

        if length <= target_length:
            return 0
            
        if idx >= len(value_counts):
            return float('inf')

        take = 1 + self.minSetSizeHelper(idx + 1, value_counts, length - value_counts[idx], target_length, memo)
        dont_take = self.minSetSizeHelper(idx + 1, value_counts, length, target_length, memo)

        memo[key] = min(take, dont_take)

        return memo[key]

class Solution:
    def minSetSize(self, arr: List[int]) -> int:


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        sizes = [ size for size in counts.values() ]
        
        total = sum(sizes)
        half = total / 2
        sizes.sort()
        count = 0
        while total > half:
            amount = sizes.pop()
            total -= amount
            count += 1
        return count

