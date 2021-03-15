# https://stackoverflow.com/questions/9255620/why-does-dijkstras-algorithm-use-decrease-key
from typing import List
graph = {
  1: {2:7, 3:9, 6:14},
  2: {1:7, 3:10, 4:15},
  3: {1:9, 2:10, 4:11, 6:2},
  4: {2:15, 3:11, 5:6},
  5: {6:9, 4:6},
  6: {1:14, 3:2, 5:9},
}


# def naive_dijkstra(graph, src):
#   unvisited = set(graph.keys())
#   distance = { node: float("inf") for node in unvisited }
#   distance[src] = 0
  
#   curr = src
#   while curr:
#     for neighbor in graph[curr]:
#       if neighbor in unvisited:
#         neighbor_attempt = distance[curr] + graph[curr][neighbor]
#         distance[neighbor] = min(distance[neighbor], neighbor_attempt)
        
#     unvisited.remove(curr)
#     curr = None
#     for next_node in unvisited:
#       if curr is None or distance[next_node] < distance[curr]:
#         curr = next_node

#   return distance

# print(naive_dijkstra(graph, 1))

from heapq import heappush, heappop
def fast_dijkstra(graph, src):
  dist = {}
  dist[src] = 0

  heap = []

  for node in graph:
    if node != src:
      dist[node] = float('inf')
    heappush(heap, (dist[node], node))

  visited = set()
  while heap:
    currDist, curr = heappop(heap)
    
    if curr in visited:
      continue

    visited.add(curr)

    for neighbor in graph[curr]:
      attempt = dist[curr] + graph[curr][neighbor]
      if attempt < dist[neighbor]:
        dist[neighbor] = attempt
        heappush(heap, (attempt, neighbor))

  print(dist)

fast_dijkstra(graph, 1)

# 1  function Dijkstra(Graph, source):
# 2      dist[source] ← 0                           // Initialization
# 3
# 4      create vertex priority queue Q
# 5
# 6      for each vertex v in Graph:          
# 7          if v ≠ source
# 8              dist[v] ← INFINITY                 // Unknown distance from source to v
# 10
# 11         Q.add_with_priority(v, dist[v])
# 12
# 13
# 14     while Q is not empty:                      // The main loop
# 15         u ← Q.extract_min()                    // Remove and return best vertex
# 16         for each neighbor v of u:              // only v that are still in Q
# 17             alt ← dist[u] + length(u, v)
# 18             if alt < dist[v]
# 19                 dist[v] ← alt
# 21                 Q.decrease_priority(v, alt)
# 22
# 23     return dist, prev

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.makeGraph(n, edges, succProb)
        
        dist = {}
        dist[start] = 1
        
        visited = set()
        
        heap = []
        
        for node in graph:
            if node != start:
                dist[node] = 0
            heappush(heap, (-dist[node], node))

        while heap:
            currDist, curr = heappop(heap)


            if curr in visited:
                continue

            if curr == end:
                break

            visited.add(curr)

            for neighbor in graph[curr]:
                attempt = dist[curr] * graph[curr][neighbor]
                if attempt > dist[neighbor]:
                    dist[neighbor] = attempt
                    heappush(heap, (-attempt, neighbor))

        return dist[end]
        
    def makeGraph(self, n, edges, succProb):
        graph = {}
        for i in range(n):
            graph[i] = {}

        for i in range(0, len(edges)):
            a, b = edges[i]
            weight = succProb[i]
            graph[a][b] = weight
            graph[b][a] = weight            

        return graph

# https://leetcode.com/problems/map-of-highest-peak/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        layers = self.findWaterLocations(isWater)
        visited = set()
        
        return self.buildGrid(layers, len(isWater), len(isWater[0]), visited)
        
    def findWaterLocations(self, isWater):
        layers = []
        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col] == 1:
                    layers.append([(row, col)])
        return layers
    
    def buildGrid(self, layers, rows, cols, visited):
        grid = []
        for row in range(rows):
            rowCon = []
            for col in range(cols):
                rowCon.append(None)
            grid.append(rowCon)
            
        for subArr in layers:
            for layer in subArr:
                grid[layer[0]][layer[1]] = 0
                visited.add((layer[0], layer[1]))
        

        current_layers = layers
        while any(current_layers):
            new_layers = []

            for layer in current_layers:
                new_layer = []
                for node in layer:
                    neighbors = self.paint(grid, node, visited)
                    new_layer += neighbors
                new_layers.append(new_layer)
            current_layers = new_layers
        return grid



    # curr_layers: [
    #   [ 01 , 12 ] <- layer
    #   [00, 11, 20 ]
    # ]

    # new_layers: [ 
    #   [ 22 ] 
    #  
    # ]

        #    0 1 2         
        #    - - -          
        # 0-[1,1,0]         visited: { (0, 2) (1, 0) (0,1) (1,2) 00, 11, 20, 22 }
        # 1-[0,1,1]
        # 2-[1,x,2]
                
    def paint(self, grid, node, visited):
        row, col = node
        curr = grid[row][col]
        top = (row - 1, col)
        bottom = (row + 1, col)
        left = (row, col - 1)
        right = (row, col + 1)
        
        newLayer = []
        if top[0] >= 0 and top not in visited:
            grid[top[0]][top[1]] = curr + 1
            visited.add(top)
            newLayer.append(top)
        if bottom[0] < len(grid) and bottom not in visited:
            grid[bottom[0]][bottom[1]] = curr + 1
            visited.add(bottom)
            newLayer.append(bottom)
        if left[1] >= 0 and left not in visited:
            grid[left[0]][left[1]] = curr + 1
            visited.add(left)
            newLayer.append(left)
        if right[1] < len(grid[0]) and right not in visited:
            grid[right[0]][right[1]] = curr + 1
            visited.add(right)
            newLayer.append(right)
        return newLayer
    
s = Solution()
print(s.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))
# [[1,1,0],[0,1,1],[1,2,2]]