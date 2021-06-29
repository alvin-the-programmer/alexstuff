from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for idx in range(len(equations)):
            firstNode = equations[idx][0]
            secondNode = equations[idx][1]
            edge = values[idx]
            
            if firstNode not in graph:
                graph[firstNode] = {}
            if secondNode not in graph:
                graph[secondNode] = {}

            graph[firstNode][secondNode] = edge
            graph[secondNode][firstNode] = 1 / edge
        
        output = []
        for query in queries:
            firstNode = query[0]
            secondNode = query[1]

            if firstNode not in graph or secondNode not in graph:
                output.append(-1)
            else:
              visited = set()
              output.append(self.traverseGraph(firstNode, secondNode, graph, visited))

        return output

    def traverseGraph(self, source, dest, graph, visited):
        if source in visited:
            return -1

        visited.add(source)

        if source == dest:
            return 1
        
        neighbors = graph[source]

        for neighbor, edge in neighbors.items(): 
            result = self.traverseGraph(neighbor, dest, graph, visited)
            if result != -1:
                return edge * result

        return -1

# Time C:
# n = # of equations
# q = # of queries
# O(n + q*n) = O(qn)

# Space:
# O(n^2 + q *(n + n) ) = O(n^2 + qn)