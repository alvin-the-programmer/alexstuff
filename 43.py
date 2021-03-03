from typing import List
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = self.convertToGraph(N, dislikes)

        visited = {}
        for node in graph:
            if node not in visited:
                if self.switchTraverse(node, graph, visited, 'blue') == False:
                    return False
        return True

    def convertToGraph(self, N, dislikes):
        graph = {}

        for i in range(1, N + 1):
            graph[i] = []

        for dislike in dislikes:
            src, dest = dislike
            graph[dest].append(src)
            graph[src].append(dest)
        
        return graph

    def switchTraverse(self, curr, graph, visited, color):
        if curr in visited:
            return visited[curr] == color
        visited[curr] = color

        neighbors = graph[curr]

        new_color = 'red' if color == 'blue' else 'blue'
        for neighbor in neighbors:
            if self.switchTraverse(neighbor, graph, visited, new_color) == False:
                return False
        
        return True




#     N things
#     2^n subsets

# [a,b] != [b,a]


# 2

# 1 2
# 2 1

# 4

# 4 x 3 x 2 x 1





# constant (1)
# logarithmic (log n)
# linear (n)
# linearthmic (n log n)
# polynomial n^2, n^c
# exponential 2^n, c^n
# factorial n!

