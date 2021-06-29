# max path sum
#
# Write a function, max_path_sum, that takes in a grid as an argument. 
# The function should return the maximum sum possible by traveling a path from the top-left corner 
# to the bottom-right corner. You may only travel through the grid by moving down or right.

# test_00:
# grid = 
# [  0  1   2
#   [1, 3, 12], 0
#   [5, 1, 1], 1
# ]

#   [3, 6, 1], 2
# ]
# max_path_sum(grid) # -> 18
"""
    16   (0,0)
       /          \
  (0,1)          (1,0)
   /  \          /   \
(1,1) (0,2)     (1,1)
  |     /   \
(1,2) (1,2) (0,3)
"""

# Brute: 
# Time O(2^(r + c))
# Space O(r + c)



# Memo: 
# Time O(rc))
# Space O(rc)


def max_path_sum(grid):
    memo = {}
    return max_path_sum_helper(grid, 0, 0, memo)

def max_path_sum_helper(grid, row, col, memo):
    if (row,col) in memo:
        return memo[(row, col)]

    row_inbounds = row < len(grid)
    col_inbounds = col < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return float('-inf')

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return grid[row][col]

    memo[(row, col)] = grid[row][col] + max(max_path_sum_helper(grid, row + 1, col, memo), max_path_sum_helper(grid, row, col + 1, memo))

    return memo[(row, col)]

# c + max(a, b) === max(a+c, b+c)

grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
# print(max_path_sum(grid)) # -> 18

grid = [
  [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
  [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
  [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# print(max_path_sum(grid)) # -> 56



# Write a function, *linked_list_cycle*, that takes in the head of a linked list as an argument. The 
# function should return a boolean indicating whether or not the linked list contains a cycle.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



# def linked_list_cycle(head):
#     visited = set()
#     curr = head

#     while curr:
#         if curr in visited:
#             return True
#         visited.add(curr)
#         curr = curr.next

#     return False


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d
d.next = b # cycle

#         _______
#       /        \
# a -> b -> c -> d 
#      s              
#                    f

# a <-> b
# f
# s

def linked_list_cycle(head):
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
          return True

    return False

print(linked_list_cycle(a))  # True

a p p a

ap
[a, p]

"pa"