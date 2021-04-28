# from collections import deque
# from typing import List
# #    0 1
# # r0[X,X]   A       queue = [(2,0,2)]  level = 1       
# # r1[X,X]
# # r2[X,1]

# # X X a
# # ! a 0
# # 0 0 0

# class Solution:
#     def shortestBridge(self, A: List[List[int]]) -> int:
#         island_a_positions = set()
#         island_b_positions = set()
#         self.find_islands(A, island_a_positions, island_b_positions, True)
#         self.find_islands(A, island_a_positions, island_b_positions, False)
        
#         return self.closestBridge(A, island_a_positions, island_b_positions)
    
#     def closestBridge(self, A, island_a_positions, island_b_positions):
#         queue = deque([ (row, col, 0) for row, col in island_a_positions ])
        
#         deltas = [(1,0), (-1, 0), (0, 1), (0, -1)]

#         visited = set([*island_a_positions])

#         while queue:
#             row, col, level = queue.popleft()
            
#             for delta in deltas:
#                 row_add, col_add = delta
#                 new_row = row + row_add
#                 new_col = col + col_add
                
#                 row_inbounds = 0 <= new_row < len(A)
#                 col_inbounds = 0 <= new_col < len(A[0])
                
#                 if row_inbounds and col_inbounds and (new_row, new_col) not in island_a_positions and (new_row, new_col) not in visited:
#                     curr = A[new_row][new_col]
#                     if (new_row, new_col) in island_b_positions:
#                         return level
#                     elif curr == 0:
#                         visited.add((new_row, new_col))
#                         queue.append((new_row, new_col, level + 1))
#         return float('inf')

#     # get_neighbors(r, c)
#     #  give back a list of inbounds neighbors
    
#     def find_islands(self, A, island_a, island_b, is_a):
#         break_flag = False
        
#         for row in range(len(A)):
#             for col in range(len(A[0])):
#                 curr = A[row][col]
#                 if is_a and curr == 1:
#                     self.df_trav(A, row, col, island_a)
#                     break_flag = True
#                     break
#                 elif is_a == False and (row,col) not in island_a and curr == 1:
#                     self.df_trav(A, row, col, island_b)
#                     break_flag = True
#                     break
#             if break_flag:
#                 break
        
#     def df_trav(self, A, row, col, island_positions):
#         row_inbounds = 0 <= row < len(A)
#         col_inbounds = 0 <= col < len(A[0])
        
#         if not row_inbounds or not col_inbounds:
#             return
        
#         if (row, col) in island_positions:
#             return
        
#         curr = A[row][col]
        
#         if curr != 1:
#             return
        
#         island_positions.add((row, col))
        
#         deltas = [(1,0), (-1,0), (0, 1), (0, -1)]
        
#         for delta in deltas:
#             row_add, col_add = delta
#             self.df_trav(A, row + row_add, col + col_add, island_positions)

#     # queue = [
#     #   'google.com/home'
#     #     'google.com/home/sadss'
#     #     'google.com/home/sdsd'
#     #     'google.com/home/asd'
#     #   'google.com/apple'
#     #   'google.com/feed.rss'
#     # ]

#     # root_url('www.google.com')
#     # 'google.com/home'
#     #   'google.com/home/'
#     #   'google.com/home/'
#     #   'google.com/home/'
#     # 'google.com/apple'
#     # 'google.com/feed.rss'
#     # find_links(url) =
#     # is_rss()

#     # def root_url(root):
#         # find_links(root)  ['google.com/feed.rss', 'google.com//home/poko.rss', 'google.com/dlsmfd']
#     #     # queue = [url1, url2, url3]
#     #     queue = [root]
#     #     while queue:
#     #       url = root.pop()
#     #       if url is rss:
#     #           retu
#     #       find_links(url)
#     #     return 'google.com/poko.rss'

#     # visited = set()
#     # # visited.add(value)
#     # visited.append(3)


#     # https://leetcode.com/problems/subarray-sum-equals-k/


# # sum(i,j)=sum(0,j)-sum(0,i)

# class Solution:
#     def subarraySum(self, nums, k) -> int:
#         sums = {}
#         curr = 0
#         for end in range(0, len(nums) + 1):
#           sums[(0, end)] = curr
#           if end != len(nums):
#             curr += nums[end]

#         count = 0
  
        
#         for i in range(len(nums) + 1):
#           if sums[(0, i)] == k:
#             count += 1


#         total = len(nums)
#         for i in range(1, len(nums) + 1):
#           if sums[(0,total)] - sums[(0,i)] == k:
#             count += 1
      
        
#         return count



# public class Solution {
#     public int subarraySum(int[] nums, int k) {
#         int count = 0, sum = 0;
#         HashMap < Integer, Integer > map = new HashMap < > ();
#         map.put(0, 1);
#         for (int i = 0; i < nums.length; i++) {
#             sum += nums[i];
#             if (map.containsKey(sum - k))
#                 count += map.get(sum - k);
#             map.put(sum, map.getOrDefault(sum, 0) + 1);
#         }
#         return count;
#     }
# }

# # https://leetcode.com/problems/subarray-sum-equals-k/

# # {
# #   0,0 : 0
# #   0,1 : a
# #   0,2 : a + b
# #   0,3 : 
# # }


# [a,b,c,d]

# # a, b, c
# #  0 1 2 3
# # [a,b,c,d]


# # (0,3)

# #  0  1  2  3
# # [a, b, c, d]
# # {
# #  (0, 0): 0
# #  (0, 1): a 
# #  (0, 2): a + b
# #  (0, 3): a + b + c
# #  (0, 4): a + b + c + d
# # }

# # (1, 4)
# # (a + b + c + d) - (a) = b + c + d



# # (1,2)

# # (0,2) - (0,1) = (a + b) - (a) = b


# # (0, 2) = sum(0, 2) - sum(0, 0)



# # sum(i,j)=sum(0,j)-sum(0,i)


# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
          return []

        queue = deque([(0, root)])
        curr_level = 0
        left = False
        levels = []
        
        while queue:
          level, node = queue.popleft()
          if level > len(levels) - 1:
            levels.append([node.val])
          else:
            levels[level].append(node.val)

          if level != curr_level:
            left = not left
            curr_level = level

          if left:
            if node.left != None:
              queue.append((level +1, node.left))
            if node.right != None:
              queue.append((level +1, node.right))
          else:
            if node.right != None:
              queue.append((level +1, node.right))
            if node.left != None:
              queue.append((level +1, node.left))

        return levels


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
          return []

        queue = deque([(0, root)])
        curr_level = 0
        left = False
        levels = []
        
        while queue:
          level, node = queue.popleft()
          if level > len(levels) - 1:
            levels.append([])
          
          if left:
            levels[level].append(node.val)
          else:
            levels[level].insert(0, node.val)

          if level != curr_level:
            left = not left
            curr_level = level

          if node.right != None:
            queue.append((level +1, node.right))
          if node.left != None:
            queue.append((level +1, node.left))

        return levels
          


          [1,2,3,4,null,null,5]

           1 
          / \
         2   3 
        /     \
      4         5


      left = False
      queue = [ 4, 5]

