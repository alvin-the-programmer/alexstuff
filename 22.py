
def min_cost_path(graph, src, dest):
    visited = set()
    return min_cost_path_helper(graph, src, dest, visited)

def min_cost_path_helper(graph, src, dest, visited):
    if src in visited:
        return float('inf')
    visited.add(src)
    
    costs = graph[src]

    if src == dest:
        return 0
    
    min_cost = float('inf')

    for neighbor in costs:
        cost_of_path = costs[neighbor] + min_cost_path_helper(graph, neighbor, dest, set(visited))
        if cost_of_path < min_cost:
            min_cost = cost_of_path
    
    return min_cost



# g1 = {
#   'a': { 'b': 7, 'e': 10, 'c': 2},
#   'b': { },
#   'c': { 'b': 6, 'd': 1 },
#   'd': { },
#   'e': { 'd': 3 }
# }

# g2 = {
#     'a' : { 'b' : 1},
#     'b' : { 'c' : 1},
#     'c' : { 'a' : 1, 'd' : 1},
#     'd' : {}
# }


# print(min_cost_path(g2, 'a', 'd')) # 3

# print(min_cost_path(g1, 'a', 'e')) # 10
# print(min_cost_path(g1, 'a', 'd')) # 3
# print(min_cost_path(g1, 'c', 'a')) # float(Infinity)


g3 = {
    "s": { "t": 1, "u": 2},
    "t": { "u": 8},
    "u": { "v": 5},
    "v": {}
}

print(min_cost_path(g3, 's', 'v')) # 7

# https://awwapp.com/b/ugkm4fi2md6dl/