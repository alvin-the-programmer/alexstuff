# https://leetcode.com/problems/is-graph-bipartite/submissions/
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        red = set()
        blue = set()
        
        for node in range(len(graph)):
            if node not in red and node not in blue:
                if self.isBipartiteHelper(graph, node, red, blue) == False:
                    return False
        return True
        
    def isBipartiteHelper(self, graph, curr, red, blue, last = -1, next_color = "red"):
        if curr in red:
            if next_color  == "blue":
                return False
            return True
        if curr in blue:
            if next_color  == "red":
                return False
            return True
       
        if next_color == "red":
            red.add(curr)
        if next_color == "blue":
            blue.add(curr)
            
        neighbors = graph[curr]
        
        for neighbor in neighbors:
            if last != neighbor:
                if curr in red:
                    if self.isBipartiteHelper(graph, neighbor, red, blue, curr, "blue") == False:
                        return False
                if curr in blue:
                    if self.isBipartiteHelper(graph, neighbor, red, blue, curr, "red") == False:
                        return False
        return True

# TIME:
# n = length of graph(# of nodes)
# ask alvin to clarify this one.
# n for the outside for loop
# another n to traverse through the graph
# but then sometimes we hit nodes that we've already seen. how do i deal with this?
# O(n^2)

# SPACE:
# O(n + n + n) = O(n)

# https://leetcode.com/problems/find-eventual-safe-states/submissions/
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        output = []
        visited = set()
        visiting = set()
        
        for node in range(len(graph)):
            if self.cyclePresent(node, graph, visited, visiting) == False:
                output.append(node)
        
        return output
    
    def cyclePresent(self, curr, graph, visited, visiting):
        if curr in visiting:
            return True
        if curr in visited:
            return False
        visiting.add(curr)
        neighbors = graph[curr]
        
        for neighbor in neighbors:
            if self.cyclePresent(neighbor, graph, visited, visiting) == True:
                return True
        visiting.remove(curr)
        visited.add(curr)
        
        return False

# TIME
# n = # of nodes
# less than O(n^2)

# SPACE:
# O(n)




# Problems i need help with
# https://leetcode.com/problems/odd-even-jump/