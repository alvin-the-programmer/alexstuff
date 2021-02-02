# graphs
# https://awwapp.com/b/uls6yh0smkwuj/


# adj list 
# g1 = {
#   "a": ["b", "c"],
#   "b": ["c"],
#   "c": ["f"],
#   "d": ["e"],
#   "e": ["d"],
#   "f": [],
#   "z": []
# }


# Write a fn that takes in a graph and a start node.
# The fn should print out all node values connected to the start node in depth first order.


# def printConnectedNodes(graph, start):
#     stack = [start]
#     visited = set()
#     while stack:
#         curr = stack.pop()
#         print(curr)
#         visited.add(curr)
#         for node in graph[curr]:
#             if node not in visited:
#                 stack.append(node)

# def printConnectedNodes(graph, start):
#     visited = set()
#     return printConnectedNodesHelper(graph, start, visited)

# def printConnectedNodesHelper(graph, start, visited):
#     if start in visited:
#      return

#     print(start)
#     visited.add(start)

#     for neighbor in graph[start]:
#         printConnectedNodesHelper(graph, neighbor, visited)

    
# printConnectedNodes(g1, 'a') # 
# print('--')
# printConnectedNodes(g1, 'd') # 


# write a fn that takes in a graph and two nodes: src and dst
# the fn should return a bool indicating whether or not there is a path that connects src to dst

def has_path(graph, start, dest):
    stack = [start]
    visited = set()

    while stack:
        curr = stack.pop()
        if curr == dest:
            return True
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False




# g1 = {
#   "a": ["b", "c"],
#   "b": ["c"],
#   "c": ["f"],
#   "d": ["e"],
#   "e": ["d"],
#   "f": [],
#   "z": []
# }

# g1 = {
#   "a": {"b": 2, "c": 4],
#   "b": {"c"], 
#   "c": {"f"],
#   "d": {"e"],
#   "e": {"d"],
#   "f": {],
#   "z": {]
# }


# print(has_path(g1, 'a', 'f')) # true
# print(has_path(g1, 'b', 'c')) # true
# print(has_path(g1, 'f', 'a')) # false
# print(has_path(g1, 'a', 'e')) # false




def printConnectedNodes(graph, start):
    visited = set()
    return printConnectedNodesHelper(graph, start, visited)

def printConnectedNodesHelper(graph, start, visited):
    if start in visited:
     return

    print(start)
    visited.add(start)

    for neighbor in graph[start]:
        printConnectedNodesHelper(graph, neighbor, visited)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
    def explore(grid, r, c, visited):
        if r > len(grid) or r < 0:
            return
        if c > len(grid[0]) or c < 0:
            return

        explore(grid, r - 1,  c)
        explore(grid, r - 1,  c)
        explore(grid, r - 1,  c)
        explore(grid, r - 1,  c)
  
  
