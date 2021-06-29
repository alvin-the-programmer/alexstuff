# Write a function, middleValue, that takes in the head of a linked list as an argument. 
# The function should return the value of the middle node in the linked list. 
# If the linked list has an even number of nodes, then return the value of the second middle node.

# You may assume that the input list is non-empty.
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# a -> b -> c -> d -> e     : 5
#           2
# middle_value(a) # c

# # a -> b -> c -> d -> e -> f      : 6
#                  3
# middle_value(a) # d

# find lengh of ll
# 5 // 2 = 2
# 6 // 2 = 3
# counter = 0
# n = # of nodes 
# 

def middle_value(head):
    length = len_of_ll(head)
    middle_node = length // 2

    curr = head
    curr_idx = 0
    while curr_idx < middle_node:
        curr = curr.next
        curr_idx += 1
    return curr.val

def len_of_ll(head):
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    return count

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# a -> b -> c -> d -> e -> NONE
#                     f
#           s 

# a -> b -> c -> d -> e -> f -> g -> h -> NONE
#                     s
#                                          f

def middle_value(head):
    slow = head
    fast = head

    while (fast is not None) and (fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

def middle_value(head):
    slow = head
    fast = head

    while not ((fast is None) or (fast.next is None)):
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

# demorgans law
# !(A && B)
# !A || !B

# #           
# print(middle_value(a)) # c


# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# a -> b -> c -> d -> e -> f


# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# print(middle_value(a)) # c




# Write a function, lefty_nodes, that takes in the root of a binary tree. 
# The function should return a list containing the left-most value on every level of the tree. 
# The list must be ordered in a top-down fashion where the root is the first item.


# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h

# breadth-level traversal
# [(a,0), (b,1) (c,1)]
# curr_level = -1
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
# lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]

from collections import deque

# def lefty_nodes(root):
#     output = []
#     curr_level = -1
#     queue = deque([ (root, 0) ])

#     while queue:
#         curr_node, level = queue.popleft()

#         if curr_level != level:
#             output.append(curr_node.val)
#             curr_level += 1
        
#         if curr_node.left:
#             queue.append((curr_node.left, level + 1))
#         if curr_node.right:
#             queue.append((curr_node.right, level + 1))
        
#     return output


def lefty_nodes(root):
    output = []
    queue = deque([ (root, 0) ])

    while queue:
        curr_node, level = queue.popleft()

        if len(output) == level:
            output.append(curr_node.val)
        
        if curr_node.left:
            queue.append((curr_node.left, level + 1))
        if curr_node.right:
            queue.append((curr_node.right, level + 1))
        
    return output

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

# print(lefty_nodes(a)) # [ 'a', 'b', 'd', 'g' ]



"""  


    a
   / \ 
  b - c


dir edges: CYCLE
 a, c
 c, b
 b, a

***dir edges: NO CYCLE
 a, c
 a, b
 b, c
"""



# Write a function, island_count, that takes in a grid containing Ws and Ls. 
# W represents water and L represents land. 
# The function should return the number of islands on the grid. 
# An island is a vertically or horizontally connected region of land.


grid = [  
  ['W', 'L', 'W', 'W', 'W'],    # set((0, 1) (1, 1), )
  ['W', 'L', 'W', 'W', 'W'],    # island_count = 0
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

# DFS


# def island_count(grid):
#     islands = 0
#     visited = set()

#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             if grid[row][col] == "L" and (row,col) not in visited:
#                 islands += 1
#                 traverse_island(grid, row, col, visited)
#     return islands

# def traverse_island(grid, row, col, visited):
#     row_inbounds = 0 <= row < len(grid)
#     col_inbounds = 0 <= col < len(grid[0])
#     if not row_inbounds or not col_inbounds:
#         return

#     if (row, col) in visited:
#         return
#     visited.add((row, col))

#     if grid[row][col] == "W":
#         return
    
#     deltas = [(0,1), (0,-1), (1,0), (-1,0)]
#     for row_add, col_add in deltas:
#         traverse_island(grid, row + row_add, col + col_add, visited)



def island_count(grid):
    islands = 0
    visited = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if traverse_island(grid, row, col, visited):
                islands += 1
    return islands

def traverse_island(grid, row, col, visited):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False

    if (row, col) in visited:
        return False
    visited.add((row, col))

    if grid[row][col] == "W":
        return False
    
    deltas = [(0,1), (0,-1), (1,0), (-1,0)]
    for row_add, col_add in deltas:
        traverse_island(grid, row + row_add, col + col_add, visited)

    return True

print(island_count(grid)) # -> 3

# TODO DP