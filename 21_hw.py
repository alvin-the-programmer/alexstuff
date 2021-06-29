class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        return self.allPathsSourceTargetHelper(graph, 0, target)
    
    def allPathsSourceTargetHelper(self, graph, curr, target):
        neighbors = graph[curr]
       
        if curr == target:
            return [[curr]]

        all_paths = []
        
        for neighbor in neighbors:
            all_paths += self.allPathsSourceTargetHelper(graph, neighbor, target)
            
        for path in all_paths:
            path.insert(0, curr)
            
        return all_paths

# https://awwapp.com/b/uvlzjexff1qzb/

# b = br factor
# n = # nodes
#
# O(b^n * n + n) -> O(b^n * n)