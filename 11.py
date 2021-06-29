# https://awwapp.com/b/ue4tr7tg06mzm/

# def tree_max(root):
#   if root == None:
#     return float('-inf')
#   return max(root.val, tree_max(root.left), tree_max(root.right))

# tree_max(five_node)

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

#       a
#     /  \
#    b    c 
#  / \     \
# d   e    f 
#     /
#    x
#
# path

# Write a fn that takes in the root of a bintree and a targetVal. The fn should return
# a bool indicating whether or not a path exists between the root and a node containing the target.

# Write a fn that takes in the root of a bintree and a targetVal. The fn should return an list
# represent a path from root to the target value. If there is not such path, then return an empty list

#       a
#     /  \
#    b    c 
#  / \     \
# d   e    f        
#     /             
#    x              

# def find_path(root, target):
#     if root is None:
#         return []
#     if root.val == target:
#         return [target]
    
#     left_path = find_path(root.left, target)
#     if left_path:
#         return [root.val] + left_path

#     right_path = find_path(root.right, target)
#     if right_path:
#         return [root.val] + right_path
#     return []

def find_path(root, target):
    answer = find_path_helper(root, target)
    return answer[::-1]

def find_path_helper(root, target):
    if root is None:
        return []
    if root.val == target:
        return [target]
    
    left_path = find_path_helper(root.left, target)
    if left_path:
        left_path.append(root.val)
        return left_path

    right_path = find_path_helper(root.right, target)
    if right_path:
        right_path.append(root.val)
        return right_path
    return []

root = a
print(find_path(root, 'x')) # [ 'a', 'b', 'e', 'x']
print(find_path(root, 'b')) # [ 'a',) 'b' ]
print(find_path(root, 'y')) # [ ]

root = Node('a')
curr = root
for i in range(900):
  curr.right = Node('a')
  curr = curr.right

curr.right = Node('q')


# print(find_path(root, 'q'))

# def print_right(root):
#   if (root is None):
#     return
#   print(root.val)
#   print_right(root.right)

# print_right(root)