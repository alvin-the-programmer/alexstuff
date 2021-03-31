class Node:
  def __init__(self, val):
    self.val = val
    self.children = []

def maxHeight(root):
    if len(root.children) == 0:
        return 0

    max = float('-inf')
    for child in root.children:
        length = 1 + maxHeight(child)
        if length > max:
            max = length
    
    return max
    


#       a
#    /   |   \  
#   b    c    d
#       / \
#       e f
#      /
#      g

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')

# a.children = [ b, c, d ]
# c.children = [ e,  f ]
# e.children = [ g ]

# print(maxHeight(a))



# https://leetcode.com/problems/number-of-islands/