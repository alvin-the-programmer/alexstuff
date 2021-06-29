"""
Given a binary tree, with characters as nodes, return the path from leaf node to root, but smallest alphabetically
for example, A is root, DEA, BAEA, BCA are all paths from leaf to the root A, but return BCA because B comes DEA and BCA is shorter than BAEA

          A
         /  \
       E     C 
      /  \   /
    D     A  B
        /
       B
Each node should have the property of:

value
left
right
should return BCA
"""

# n = # of nodes
# O(n * (n + n))

def find_smallest_word(root):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  output = sorted(find_smallest_word_helper(root, alphabet))

  return output[0]

def find_smallest_word_helper(root, alphabet):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [alphabet[root.val]]

  left = find_smallest_word_helper(root.left, alphabet) #['D]
  right = find_smallest_word_helper(root.right, alphabet) #[B]

  output = left + right
  new_output = []
  for word in output:
    new_output.append(word + alphabet[root.val])

  return new_output


  
  

# O (n^2 + n^2*logn)




class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

    #        A
    #      /   \
    #    E      C 
    #   /  \   /
    # D    A  B
    #     /
    #    B

a = Node('A')
b = Node('E')
c = Node('C')
d = Node('D')
e = Node('A')
f = Node('B')
g = Node('B')
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
e.left = g

# BCA
print(find_smallest_word(a))

# BA
# ABC


(l, c)

           1 (0,0)
         /   \
  (1, -1)  3     2 (1, 1)
       / \        \  
(2,-2)5   3 (2,0)  9 (2, 2)


[
  0: [(0,0)],
  1: [(1, )]
]

[(0,0) (1,-1) (1,1) (2,-2) (2,0) (2, 2)]


         1 (0,0)
         / \
 (1,-1) 3   2 (1,1)
       /        
 (2,-2)5      

 [
   0[(0)]
   [-1,1]
   [(2,-2)]
 ]

if len(1) ret 1
 return max([ 1, 2, 1])


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        stack = [(root, 0, 0)]
        counts = {}
        while stack:
          curr, level, col = stack.pop()
          if level not in counts:
            counts[level] = []
          counts[level].append(col)
          
          if curr.left is not None:
            stack.append((curr.left, level + 1, col - 2))
          if curr.right is not None:
            stack.append((curr.right, level + 1, col + 2))
        output = []
        for count in counts:
          level = counts[count]
          if len(level) == 1:
            output.append(1)
          else:
            output.append(abs(min(level) - max(level)))

        return max(output)
        
actual 6
expect 8

[1,1,1, 1,null,null,1,    1,null,null,1]


                  1
              /       \
             1         1
          /    \      /  \
        1       null null 1
      / \               /     \
    1   null  n n  n n     null    1