def min_path_cost(graph, src, dst):
    unvisited = set(graph.keys()) # 1.
    distance = {node: float("inf") for node in unvisited} # 2.
    distance[src] = 0

    curr = src
    while curr:
        for neighbor in graph[curr]: # 3.
            if neighbor in unvisited:
                neighbor_attempt = distance[curr] + graph[curr][neighbor]
                distance[neighbor] = min(distance[neighbor], neighbor_attempt)

        unvisited.remove(curr) # 4.
        curr = None

        for next_node in unvisited: # 6.
            if curr is None or distance[next_node] < distance[curr]:
                curr = next_node

    return distance

# 1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
# 2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.[16]
# 3. For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbour B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
# 4. When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
# 5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
# 6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.


graph = {
    1: {2: 7, 3: 9, 6: 14},
    2: {1: 7, 3: 10, 4: 15},
    3: {1: 9, 2: 10, 4: 11, 6: 2},
    4: {2: 15, 3: 11, 5: 6},
    5: {6: 9, 4: 6},
    6: {1: 14, 3: 2, 5: 9},
}

print(min_path_cost(graph, 1, 5))

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
