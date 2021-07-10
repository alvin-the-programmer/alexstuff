# https://leetcode.com/problems/complete-binary-tree-inserter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.level = 0
        self.curr_level_count = 1
        
    def insert(self, v: int) -> int:
        new_node = TreeNode(v)
        parent = self.bfs(self.root)
        
        if parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node
        
        return parent.val
        
    def bfs(self, root):
        queue = deque([(root, 0)])
        
        while queue:
            curr, level = queue.popleft()
            
            if curr.left:
                queue.append((curr.left, level + 1))
            else:
                return curr
            
            if curr.right:
                queue.append((curr.right, level + 1))
            else:
                return curr
            
        return None
    
    def get_root(self) -> TreeNode:
        return self.root


from collections import deque
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.nodes = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            self.nodes.append(curr)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
    
        

    def insert(self, v: int) -> int:
        
        pos = len(self.nodes)
        new_node = TreeNode(v)
        self.nodes.append(new_node)
        if pos % 2 == 0:
            parent = self.nodes[int((pos-2) / 2) ]
            parent.right = new_node
        else:
            parent = self.nodes[int((pos-1) / 2) ]
            parent.left = new_node
        return parent.val
            

    def get_root(self) -> TreeNode:
        return self.nodes[0]
        
#             0
#         /     \
#        1      2   
#       / \    / \
#      3   4  5   6
#     /      
#    (7)       
#           
#           
#           
#           

# [0 1 2 3 4 5 6]


#             (i)
#            /   \
#      (2i + 1)   (2i + 2)



# (7 - 1) / 2 = 3

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()


# https://leetcode.com/problems/find-and-replace-in-string/

import heapq

# n = # of indices
# s = length of s
# n log n
# x = longest target

# slog(n)

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        heap = []
        
        for idx in range(len(indices)):
            word_beg = indices[idx]
            source = sources[idx]
            target = targets[idx]
            
            if s[word_beg:].startswith(source):
                heapq.heappush(heap, (word_beg, source, target))
        
        new_s = []
        idx = 0
        
        while idx < len(s):
            if heap and heap[0][0] == idx:
                word_beg, source, target = heapq.heappop(heap)
                new_s.append(target)
                idx += len(source)
            else:
                new_s.append(s[idx])
                idx += 1
                
        return ''.join(new_s)




# indices = [0, 2]
# {0: 0, 2: 1}
def findReplaceString(s, indices, sources, targets):
  index_map = { indices[i]: i for i in range(len(indices)) }
  output = []
  i = 0
  while i < len(s):
    
    if i in index_map:
      current = index_map[i]
      if s[i:i + len(sources[current])] == sources[current]:
        source = sources[current]
        target = targets[current]
        output.append(target)
        i += len(source)
      else:
        output.append(s[i])
        i += 1
    else:
      output.append(s[i])
      i += 1

  return ''.join(output)


#   https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/



# Customer Obsession
# Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers.


# Ownership
# Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say “that’s not my job".


# Invent and Simplify
# Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by “not invented here". As we do new things, we accept that we may be misunderstood for long periods of time.


# Are right, A Lot
# Leaders are right a lot. They have strong judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs.


# Learn and Be Curious
# Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them.


# Hire and Develop the Best
# Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others. We work on behalf of our people to invent mechanisms for development like Career Choice.


# Insist on the Highest Standards
# Leaders have relentlessly high standards - many people may think these standards are unreasonably high. Leaders are continually raising the bar and driving their teams to deliver high quality products, services and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed.


# Think Big
# Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers.


# Bias for Action
# Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking.


# Frugality
# Accomplish more with less. Constraints breed resourcefulness, self-sufficiency and invention. There are no extra points for growing headcount, budget size or fixed expense.


# Earn Trust
# Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Leaders do not believe their or their team’s body odor smells of perfume. They benchmark themselves and their teams against the best.


# Dive Deep
# Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them.


# Have Backbone; Disagree and Commit
# Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly.

# Deliver Results
# Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle.


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)

        horizontalCuts.sort()
        
        verticalCuts.append(0)
        verticalCuts.append(w)

        verticalCuts.sort()
       
        max_hori_width = 0
        max_vert_width = 0

        for idx in range(len(horizontalCuts) - 1):
            left = horizontalCuts[idx]
            right = horizontalCuts[idx + 1]

            width = right - left

            if width > max_hori_width:
                max_hori_width = width

        for idx in range(len(verticalCuts) - 1):
            left = verticalCuts[idx]
            right = verticalCuts[idx + 1]

            width = right - left

            if width > max_vert_width:
                max_vert_width = width

        return (max_hori_width * max_vert_width) % ((10**9) + 7)


# https://leetcode.com/problems/subtree-of-another-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        