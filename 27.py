# https://awwapp.com/b/uy0bvbyhl0oad/
def has_cycle(graph, source):
    visiting = set()
    visited = set()
    return has_cycle_helper(graph, source, visiting, visited)
    
def has_cycle_helper(graph, source, visiting, visited):
    if source in visiting:
        return True
    if source in visited:
        return False
    neighbors = graph[source]
    
    visiting.add(source)

    for neighbor in neighbors:
        if has_cycle_helper(graph, neighbor, visiting, visited) == True:
            return True
    visiting.remove(source)
    visited.add(source)
    return False

g1 = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["d"],
  "d": ["e"],
  "e": ["b"]
}

g2 = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["d"],
  "d": ["e"],
  "e": []
}

print(has_cycle(g1, "a"))

print(has_cycle(g2, "a"))

# https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/

# https://leetcode.com/problems/course-schedule/