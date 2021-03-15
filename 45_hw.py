# https://leetcode.com/problems/number-of-islands/
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         visited = set()
#         count = 0
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if self.numIslandsHelpers(row, col, grid, visited) == True:
#                     count += 1
#         return count
        
#     def numIslandsHelpers(self, row, col, grid, visited):
#         if row < 0 or row > len(grid) - 1:
#             return False
#         if col < 0 or col > len(grid[0]) - 1:
#             return False
        
#         curr = (row, col)
        
#         if curr in visited:
#             return False
        
#         if grid[row][col] == '1':
#             visited.add(curr)
            
#             top = self.numIslandsHelpers(row - 1, col, grid, visited)
#             bottom = self.numIslandsHelpers(row + 1, col, grid, visited)
#             left = self.numIslandsHelpers(row, col - 1, grid, visited)
#             right = self.numIslandsHelpers(row, col + 1, grid, visited)
            
#             return True
#         else:
#             return False
        
# # https://leetcode.com/problems/binary-tree-right-side-view/
# # first attempt with BFS
# # from collections import deque
# # class Solution:
# #     def rightSideView(self, root: TreeNode) -> List[int]:
# #         queue = deque([root])
        
# #         arr = []
# #         while queue:
# #             last = queue[-1]
            
# #             if km:
# #                 arr.append(last.val)
            
# #             front = queue.popleft()
            
# #             left = front.left
# #             right = front.right
            
# #             if left != None:
# #                 queue.append(left)
# #             if right != None:
# #                 queue.append(right)
                
# #         return arr

# # second attempt with DFS and object?
# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         obj = {}
#         level = 0
#         finalObj = self.traverse(level, root, obj)
        
#         output = []
        
#         if not finalObj:
#             return output
        
#         for key in finalObj:
#             output.append(finalObj[key])
        
#         return output
        
#     def traverse(self, level, root, obj):
#         # print(level, root, obj)
        
#         if root is None:
#             return
        
#         obj[level] = root.val
            
#         left = self.traverse(level + 1, root.left, obj)
#         right = self.traverse(level + 1, root.right, obj)
        
#         return obj

from typing import List

# https://leetcode.com/problems/merge-k-sorted-lists/submissions/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# [[],[1]]
# []
# Expected:
# [1]


# k = # of linked lists
# n = max length of a single linked list

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # [ None ]
    
        dummyHead = ListNode(None)
        curr = dummyHead
        heads = set(lists) # O(k)
        if None in heads:
            heads.remove(None)

        while heads: # O(nk)
            minHead = ListNode(float('inf'))
            for head in heads: # O(k)
                if head.val < minHead.val:
                    minHead = head
            if minHead.next is not None:
                heads.add(minHead.next)
            heads.remove(minHead)
            curr.next = minHead
            curr = curr.next
        return dummyHead.next

    
