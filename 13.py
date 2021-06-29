class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
x = Node('x')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = x
root = a

#       3
#     /  \
#    7    2 
#  / \     \
# 10  3     4
#    /
#   1

# Write a fn that takes in a bin tree and a targetVal and returns a list representing a path from
# the root to that target. if the target is not found, then return empty list


#       a
#     /  \
#    b    c 
#  / \     \
# d   e     f
#    /
#   x


def get_path(root, target):
  q = [ root ]
  parent = { root.val: None } 
  while q:
    curr = q.pop()
    if curr.val == target:
      path = []
      curr_node = target
      while curr_node:
          path.insert(0, curr_node)
          curr_node = parent[curr_node]
      return path
    if curr.left is not None:
      q.insert(0, curr.left)
      parent[curr.left.val] = curr.val
    if curr.right is not None:
      q.insert(0, curr.right)
      parent[curr.right.val] = curr.val

  
#   return []
    
print(get_path(root, 'x')) # [a,b,e,x]
