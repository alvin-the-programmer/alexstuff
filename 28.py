# https://awwapp.com/b/umh4ufeqllrgt/
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.convertToGraph(numCourses, prerequisites)

        visited = set()
        visiting = set()

        for node in graph:
            if self.hasCycle(graph, node, visited, visiting) == True:
                return False
        return True

    def convertToGraph(self, numCourses, prereqs):
        graph = {}
        for num in range(numCourses):
            graph[num] = []

        for prereq in prereqs:
            dest = prereq[0]
            source = prereq[1]
            
            graph[source].append(dest)

        return graph

    def hasCycle(self, graph, node, visited, visiting):
        if node in visiting:
            return True
        if node in visited:
            return False

        neighbors = graph[node]

        visiting.add(node)

        for neighbor in neighbors:
            if self.hasCycle(graph, neighbor, visited, visiting) == True:
                return True

        visiting.remove(node)
        visited.add(node)

        return False

# TIME
# n = numCourses
# n^2 = prereqs
# O(n^2)

# SPACE
# O(n^2)


# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        