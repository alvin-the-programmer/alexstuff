# binary tree level order traversal
# reverse level order traversal

# reverse a linked list
def reverse(head):
    # TODO: Write your code here
    orig_order = ll_to_list(head)

    for i in range(len(orig_order) - 1, 0, -1):
        curr = orig_order[i]
        curr.next = orig_order[i - 1]

    orig_order[0].next = None
    return orig_order[-1]


def ll_to_list(curr):
    if curr is None:
        return []
# time:
# O(n)
# space:
# O(n)


# ALT SOL
def reverse(head):
    # TODO: Write your code here
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
# time:
# O(n)
# space:
# O(1)

# Topological Sort (medium)
# my solution


def topological_sort(vertices, edges):
    # TODO: Write your code here
    graph = create_indegree_graph(vertices, edges)
    sortedOrder = []
    visited = set()
    while len(sortedOrder) < len(graph):
        for node in graph:
            if len(graph[node]) == 0 and node not in visited:
                sortedOrder.append(node)
                visited.add(node)
                for parent_node in graph:
                    if node in graph[parent_node]:
                        graph[parent_node].remove(node)

    return sortedOrder


def create_indegree_graph(vertices, edges):
    graph = {}

    for i in range(vertices):
        graph[i] = set()

    for edge in edges:
        src, dest = edge
        graph[dest].add(src)
    return graph

# THEIR SOLUTION


def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1  # increment child's inDegree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:  # get the node's children to decrement their in-degrees
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder


# binary tree level order traversal
# reverse level order traversal
# zigzag traversal
# reverse a linked list
# top sort

# in progress:
# knapsack (DP problem)

def merge_sort(arr):
    return merge_sort_helper(arr, 0, len(arr) - 1)


def merge_sort_helper(arr, start, end):
    if start == end:
        return [arr[start]]

    # if start == end:
    #     return arr[start]

    middle = (start + end) // 2
    left = merge_sort_helper(arr, start, middle)
    right = merge_sort_helper(arr, middle + 1, end)

    return merge(left, right)


def merge(left, right):
    new_arr = []

    l_idx = 0
    r_idx = 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            new_arr.append(left[l_idx])
            l_idx += 1
        else:
            new_arr.append(right[r_idx])
            r_idx += 1

    return new_arr + left[l_idx:] + right[r_idx:]

# print(merge([5, 4, 3], [2, 4, 5]))


print(merge_sort([5, 2, 3, -5, -3, 1, 4, 2, 3]))
# 0  1  2  3  4  5


# [5][2]
