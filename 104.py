# class TrieNode:
#     def __init__(self, val = None, end = False):
#         self.children = {}
#         self.val = val
#         self.end = end
        
# class FileSystem:
#     def __init__(self):
#         self.root = TrieNode()
        
#     def createPath(self, path, value):
#         curr = self.root
#         paths = path[1:].split('/')
#         idx = 0
        
#         while idx < len(paths):
#             curr_path = paths[idx]
#             print(paths)
            
#             if idx == (len(paths) - 1):  
#                 if curr_path not in curr.children:
#                     curr.children[curr_path] = TrieNode(value, True)
#                     return True
                
#             if curr_path not in curr.children:
#                 return False
#             curr = curr.children[curr_path]
#             idx += 1
        
#     def get(self, path):
#         curr = self.root
#         paths = path[1:].split('/')
#         idx = 0
#         while idx < len(paths):
#             curr_path = paths[idx]
#             if curr_path not in curr.children:
#                 return -1
#             curr = curr.children[curr_path]
#             idx += 1
#         return curr.val
        

# class Node:
#     def __init__(self, val = None):
#         self.val = val
#         self.children = {}

# class FileSystem:
#     def __init__(self):
#         self.root = Node()
        

#     def createPath(self, path: str, value: int) -> bool:
#         directories = path.split('/')[1:]
        
#         current_node = self.root
#         for directory in directories[:-1]:
#             if directory in current_node.children:
#                 current_node = current_node.children[directory]
#             else:
#                 return False
        
#         new_dir = directories[-1]
#         if new_dir in current_node.children:
#             return False
#         else:
#             current_node.children[new_dir] = Node(value)
#             return True
                

#     def get(self, path: str) -> int:
#         directories = path.split('/')[1:]
        
#         current_node = self.root
#         for directory in directories:
#             if directory in current_node.children:
#                 current_node = current_node.children[directory]
#             else:
#                 return -1
#         return current_node.val
        
    
# class FileSystem:

#     def __init__(self):
#         self.root = ({}, None)
        

#     def createPath(self, path: str, value: int) -> bool:
#         directories = path.split('/')[1:]
#         current_directory = self.root
#         for directory in directories[:-1]:
#             if directory in current_directory[0]:
#                 current_directory = current_directory[0][directory]
#             else:
#                 return False
#         last_dir = directories[-1]
#         if last_dir in current_directory[0]:
#             return False
#         else:
#             current_directory[0][last_dir]= ({}, value)
#             return True
        
        
#     def get(self, path: str) -> int:
#         directories = path.split('/')[1:]
#         current_directory = self.root
#         for directory in directories:
#             if directory in current_directory[0]:
#                 current_directory = current_directory[0][directory]
#             else:
#                 return -1

#         return current_directory[1]



# https://leetcode.com/problems/max-area-of-island/

# class Solution1:
#     def maxAreaOfIsland(self, grid):
#         visited = set()
#         max_area = 0
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 curr_area = self.find_area_island(grid, row, col, visited)
#                 if curr_area > max_area:
#                     max_area = curr_area
#         return max_area

#     def find_area_island(self, grid, row, col, visited):
#         row_inbounds = 0 <= row < len(grid)
#         col_inbounds = 0 <= col < len(grid[0])

#         if not row_inbounds or not col_inbounds:
#             return 0

#         if grid[row][col] == 0:
#             return 0

#         if (row, col) in visited:
#             return 0

#         visited.add((row, col))

#         total_area = 1
#         deltas = [(0,1), (0,-1), (1,0), (-1,0)]

#         for row_add, col_add in deltas:
#             total_area += self.find_area_island(grid, row + row_add, col + col_add, visited)
        
#         return total_area



# class Solution2:
#     def minAreaOfIsland(self, grid):
#         visited = set()
#         min_area = float('inf')

#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 curr_area = self.find_area_island(grid, row, col, visited)
#                 if 0 < curr_area < min_area:
#                     min_area = curr_area

#         return 0 if min_area == float('inf') else min_area

#     def find_area_island(self, grid, row, col, visited):
#         row_inbounds = 0 <= row < len(grid)
#         col_inbounds = 0 <= col < len(grid[0])

#         if not row_inbounds or not col_inbounds:
#             return 0

#         if grid[row][col] == 0:
#             return 0

#         if (row, col) in visited:
#             return 0

#         visited.add((row, col))

#         total_area = 1
#         deltas = [(0,1), (0,-1), (1,0), (-1,0)]

#         for row_add, col_add in deltas:
#             total_area += self.find_area_island(grid, row + row_add, col + col_add, visited)
        
#         return total_area


# s = Solution2()
# # res = s.minAreaOfIsland([
# #     [0,0,0,0,0,1],
# #     [0,1,0,0,0,0],
# #     [0,1,1,0,1,0],
# #     [0,0,1,0,1,0],
# #     [0,0,0,0,0,0]
# # ])

# # print(res)

# res = s.minAreaOfIsland([
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ])

# print(res)


class Solution1:
    def maxAreaOfIsland(self, grid):
        visited = set()
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr_area = self.find_area_island(grid, row, col, visited)
                if curr_area > max_area:
                    max_area = curr_area
        return max_area

    def find_area_island(self, grid, row, col, visited):
        row_inbounds = 0 <= row < len(grid)
        col_inbounds = 0 <= col < len(grid[0])

        if not row_inbounds or not col_inbounds:
            return 0

        if grid[row][col] == 0:
            return 0

        if (row, col) in visited:
            return 0

        visited.add((row, col))

        total_area = 1
        deltas = [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (1,1), (1, -1), (-1, 1)]

        for row_add, col_add in deltas:
            total_area += self.find_area_island(grid, row + row_add, col + col_add, visited)
        
        return total_area

s = Solution1()
res = s.maxAreaOfIsland([
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
])

print(res)


def island_areas(grid):
    for row in range(len(grid)):
        for col in range(len(grid)[0]):



island_reas(grid) # [1, 4, 4,  5, 11]