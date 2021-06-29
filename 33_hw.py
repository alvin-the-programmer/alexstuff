# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/submissions/

# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         components = []
#         for i in range(n): # O(n)
#             components.append(i)
        
#         for edge in edges: # O(n^2)
#             child, parent = edge
            
#             child_parent = self.findParent(components, child) # O(n)
#             parent_parent = self.findParent(components, parent)
            
#             components[child_parent] = components[parent_parent]
        
#         counter = 0
#         for child, parent in enumerate(components): # O(n)
#             if child == parent:
#                 counter += 1
#         return counter
        
# #       [1 2 2 3 4]
# #        0 1 2 3 4

#     def findParent(self, components, n): 
#         # x = length of components
#         # time complexity: O(x)
#         # space complexity: O(x)
#         if components[n] == n:
#             return n
#         return self.findParent(components, components[n])

# # time: O(n^3)
# # space: O(n)

# # https://leetcode.com/problems/number-of-islands/

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         parents = {}
#         # space:
#         # O(rc)
#         # r = row
#         # c = col
#         for row in range(len(grid)):
#             for col in range(len(grid[0])): # time: O(rc)
#                 pos = (row, col)
#                 parents[pos] = (row, col)
                
#         for row in range(len(grid)):
#             for col in range(len(grid[0])): #O(rc^2)
#                 if grid[row][col] == "1":
#                     self.union_neighbor(grid, parents, (row, col), (row, col - 1))
#                     self.union_neighbor(grid, parents, (row, col), (row, col + 1))
#                     self.union_neighbor(grid, parents, (row, col), (row - 1, col))
#                     self.union_neighbor(grid, parents, (row, col), (row + 1, col))
#                 else:
#                     parents[(row,col)] = None
                    
#         counter = 0
        
#         for child in parents:
#             if child == parents[child]:
#                 counter += 1
                
#         return counter

#     def union_neighbor(self, grid, parents, node, neighbor):
#         nRow, nCol = neighbor
#         is_nRow_inbounds = 0 <= nRow < len(grid)
#         is_nCol_inbounds = 0 <= nCol < len(grid[0])

#         if not (is_nRow_inbounds and is_nCol_inbounds):
#             return

#         if grid[nRow][nCol] != "1":
#             return

#         self.union(parents, node, neighbor)

                    
#     def union(self, parents, child, parent): 
#         child_parent = self.find(parents, child)
#         parent_parent = self.find(parents, parent)
        
#         parents[child_parent] = parent_parent

#     def find(self, parents, child): # O(r+c) for space AND time
#         if parents[child] == child:
#             return child
#         return self.find(parents, parents[child])

    # time
    # O(rc^2)
    # space
    # O(rc)

# https://leetcode.com/problems/redundant-connection/submissions/

# Input: [[1,2], [1,3], [2,3]]

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        components = {}

        for edge in edges:
            nodeA, nodeB = edge
            components[nodeA] = nodeA
            components[nodeB] = nodeB
        
        for edge in edges:
            nodeA, nodeB = edge
            if self.find(components, nodeA) != self.find(components, nodeB):
                self.union(components, nodeA, nodeB)
            else:
                return edge
        
    def find(self, components, node):
        if components[node] == node:
            return node
        return self.find(components, components[node])
        
    def union(self, components, nodeA, nodeB):
        nodeA_parent = self.find(components, nodeA)
        nodeB_parent = self.find(components, nodeB)

        components[nodeA_parent] = nodeB_parent

        # [[1,2],[1,3],[2,3]]
        # [1,2]

s = Solution()
print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
