# https://leetcode.com/problems/path-with-maximum-probability/
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        return self.maxProb(n, edges, succProb, start, end)
        
    def maxProb(self, N, edges, probs, start, end):
        graph = self.convertToGraph(N, edges, probs)
        visited = set()
        return self.traverse(graph, start, end, visited)

    def traverse(self, graph, curr, dest, visited):
        if curr in visited:
            return 0
        if curr == dest:
            return 1
        visited.add(curr)
        neighbors = graph[curr]
        max = 0
        for neighborAndWeight in neighbors:
            neighbor, weight = neighborAndWeight
            output = weight * self.traverse(graph, neighbor, dest, set(visited))
            if output > max:
                max = output
        return max

    def convertToGraph(self, N, edges, probs):
        graph = {}
        for i in range(N):
            graph[i] = []
        for idx, edge in enumerate(edges):
            src, dest = edge
            prob = probs[idx]

            graph[src].append((dest, prob))
            graph[dest].append((src, prob))
        return graph


# BFS
from collections import deque

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.convertToGraph(n, edges, succProb)
        return self.bfs(graph, start, end)
        
    def bfs(self, graph, start, end):
        queue = deque([start])
        parents = {
            start: 1
        }
        
        while queue:
            curr = queue.popleft()            
            neighbors = graph[curr]

            for neighbor in neighbors:
                neighborAttempt = parents[curr] * graph[curr][neighbor]
                if neighbor not in parents or parents[neighbor] < neighborAttempt:       
                    if neighbor not in parents:
                        queue.append(neighbor)
                    parents[neighbor] = neighborAttempt
        
        if end in parents:
            return parents[end]
        else:
            return 0
        
    def convertToGraph(self, n, edges, succProb):
        graph = {}
        
        for idx in range(n):
            graph[idx] = {}
            
        for idx, edge in enumerate(edges):
            src, dest = edge
            graph[src][dest] = succProb[idx]
            graph[dest][src] = succProb[idx]
        
        return graph

# 3
# [[0,1],[1,2],[0,2]]
# [0.5,0.5,0.2]
# 0
# 2

# curr = 0
# queue = [1]
# neighbors = 2
# parents {
#     0: 1
#     1: 0.5
#     2: 0.2
# }


# OR
#   true or true -> true
#   false or true -> true
#   false or false -> false

# AND
#   true and true -> t
#   false and true -> f
#   false and false -> f





# Boolean Logical Operators
#   and or not, && || !
#
# They short circuit
# 
# A && B
#   -> if A is false, dont eval B
#   -> if A is true, eval B
#
# A || B
#   -> if A is true, dont eval B
#   -> if A is false, eval B




