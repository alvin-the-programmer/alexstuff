# https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        unionObj = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                pos = (row, col)
                if grid[row][col] == 1:
                    unionObj[pos] = pos
                else:
                    unionObj[pos] = None
             
                    
        # O(nm * (nm)) -> O((nm)^2)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if row - 1 >= 0:
                        if grid[row - 1][col] == 1:
                            self.union(unionObj, (row, col), (row - 1, col))
                    if row + 1 < len(grid):
                        if grid[row + 1][col] == 1:
                            self.union(unionObj, (row, col), (row + 1, col))
                    if col - 1 >= 0:
                        if grid[row][col - 1] == 1:
                            self.union(unionObj, (row, col), (row, col - 1))
                    if col + 1 < len(grid[0]):
                        if grid[row][col + 1] == 1:
                            self.union(unionObj, (row, col), (row, col + 1))
        
        # O(nm * (nm)) -> O((nm)^2)
        islandCount = {}
        for island in unionObj:
            child = unionObj[island]
            if child != None:
                captain = self.find(child, unionObj)
                if captain in islandCount:
                    islandCount[captain] += 1
                else:
                    islandCount[captain] = 1
                    
        if islandCount.values():
            return max(islandCount.values())
        else:
            return 0
            
                    
    def find(self, curr, unionObj):
        if unionObj[curr] == curr:
            return curr
        parent = unionObj[curr]
   
        return self.find(parent, unionObj)
        
    def union(self, unionObj, parent, child):
        parent_parent = self.find(parent, unionObj)
        child_parent = self.find(child, unionObj)
        
        unionObj[child_parent] = parent_parent
        return unionObj

# union find with path compression

# https://leetcode.com/problems/path-with-maximum-probability

from collections import deque

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.convertToGraph(n, edges, succProb)
        return self.dijkstra(graph, start, end)
    
    def dijkstra(self, graph, start, end):
        shortest_dist = {}
        track_pred = {}
        unvisited_nodes = graph
        
        for node in unvisited_nodes:
            shortest_dist[node] = float('-inf')
        shortest_dist[start] = 1
        
        visited_nodes = set()
        
        while unvisited_nodes:
            max_dist_node = None
            for node in unvisited_nodes:
                if max_dist_node is None:
                    max_dist_node = node
                elif shortest_dist[node] > shortest_dist[max_dist_node]:
                    max_dist_node = node
                
            path_options = graph[max_dist_node].items()
            
            for child_node, weight in path_options:
                if child_node not in visited_nodes:
                    if weight * shortest_dist[max_dist_node] > shortest_dist[child_node]:
                        shortest_dist[child_node] = weight * shortest_dist[max_dist_node]
                        track_pred[child_node] = max_dist_node
                
            unvisited_nodes.pop(max_dist_node)
            visited_nodes.add(max_dist_node)
        
        if shortest_dist[end] != float('-inf'):
            return shortest_dist[end]
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


class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    num_rows = len(grid);
    num_cols = len(grid[0]);

    leader = {}
    size = {}
    for r in range(num_rows):
       for c in range(num_cols):
          if grid[r][c] == 1:
            pos = (r, c)
            leader[pos] = pos
            size[pos] = 1

    def union(node_a, node_b):
      leader_a = find(node_a)
      leader_b = find(node_b)
      if leader_a != leader_b:
        leader[leader_b] = leader_a
        size[leader_a] += size[leader_b]

    def find(node):
      if leader[node] == node:
        return node
      return find(leader[node])

    for r in range(num_rows):
      for c in range(num_cols):
        if grid[r][c] == 1:
          if r < num_rows - 1 and grid[r + 1][c] == 1:
            union((r, c), (r + 1, c))
          if c < num_cols - 1 and grid[r][c + 1] == 1:
            union((r, c), (r, c + 1))

    return max(size.values())


def max_path_cost(graph, src, dst):
    unvisited = set(graph.keys()) # 1.
    distance = {node: 0 for node in unvisited} # 2.
    distance[src] = 1

    curr = src
    while curr is not None:
        for neighbor in graph[curr]: # 3.
            if neighbor in unvisited:
                neighbor_attempt = distance[curr] * graph[curr][neighbor]
                distance[neighbor] = max(distance[neighbor], neighbor_attempt)

        unvisited.remove(curr) # 4.
        curr = None

        for next_node in unvisited: # 6.
            if curr is None or distance[next_node] > distance[curr]:
                curr = next_node

    return distance[dst]


