# class Solution:
#     def diameterOfBinaryTree(self, root) -> int:
#         longest_path = [0]
        
#         self.df_trav(root, longest_path)
        
#         return longest_path[0]
        
#     def df_trav(self, root, longest_path):
#         if root is None:
#             return 0
        
#         left = self.df_trav(root.left, longest_path)
#         right = self.df_trav(root.right, longest_path)
        
#         new_path = left + right
        
#         if new_path > longest_path[0]:
#             longest_path[0] = new_path
        
#         return 1 + max(left, right)# https://leetcode.com/problems/longest-univalue-path/

# class Solution:
#     def longestUnivaluePath(self, root) -> int:
#         longest_path = [0]

#         self.df_trav(root, longest_path)
#         return longest_path[0]

#     def df_trav(self, root, longest_path):
#       if root is None:
#         return 0

#       left_child = self.df_trav(root.left, longest_path)
#       right_child = self.df_trav( root.right, longest_path)
#       left, right = 0, 0
      
#       if root.left is not None and root.val == root.left.val:
#         left = left_child
#       if root.right is not None and root.val == root.right.val:
#         right = right_child

#       path = left + right
#       if path > longest_path[0]:
#         longest_path[0] = path

#       return 1 + max(left, right)

# # longest: 2

# #            1
# #          /   \  2
# #         4     (5) 1
# #       /   \     \
# #      4     4     5
# # (1)
# # LC:2 RC: 2
# # L:1  R:1

# # (5)
# # LC:0 RC: 1
# # L:0  R:1
# # path: 1


# # path = 1 + 1 = 2


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def is_univalue_list(head):
#   prev = head
#   curr = head.next

#   while curr:
#     if prev.val != curr.val:
#       return False
#     prev = curr
#     curr = curr.next
#   return True

# def is_univalue_list(head, prev = None):
#   if head is None:
#     return True
  
#   if prev is not None:
#     if prev.val != head.val:
#       return False

#   return is_univalue_list(head.next, head)

# a = Node(7)
# b = Node(7)
# c = Node(7)

# a.next = b
# b.next = c

# # 7 -> 7 -> 7

# # print(is_univalue_list(a)) # True

# a = Node(7)
# b = Node(7)
# c = Node(4)

# a.next = b
# b.next = c

# # 7 -> 7 -> 4

# # print(is_univalue_list(a)) # False

# u = Node(2)
# v = Node(2)
# w = Node(3)
# x = Node(3)
# y = Node(2)

# u.next = v
# v.next = w
# w.next = x
# x.next = y

# # 2 -> 2 -> 3 -> 3 -> 2

# # print(is_univalue_list(u)) # False


# # https://leetcode.com/problems/shortest-way-to-form-string/


# # source = "abc", target = "a b c b c"
# #                           0 1 2 3 4

# # [a, ab, ac, b, bc, c, abc, '']


# # a, b, c
# # ab, ac, bc
# # abc

# # abc
# # ac

# class Solution:
#     def shortestWay(self, source: str, target: str, idx = 0) -> int:
#       word_bank = self.wordBank(source)
#       output = self.shortestWayHelper(word_bank, target, 0)
#       return -1 if output == float('inf') else output

#     def shortestWayHelper(self, wordBank, target: str, idx):
#       if idx >= len(target):
#         return 0

#       longest_prefix = ''
#       curr_target = target[idx:]
#       for word in wordBank:
#         if curr_target.startswith(word) and len(word) > len(longest_prefix):
#           longest_prefix = word

#       if longest_prefix == '':
#         return float('inf')

#       new_idx = idx + len(longest_prefix)

#       return 1 + self.shortestWayHelper(wordBank, target, new_idx)


#     # def shortestWayHelper(self, wordBank, target: str, idx):
#     #   if idx >= len(target):
#     #     return 0

#     #   longest_prefix = ''
#     #   curr_target = target[idx:]
#     #   for word in wordBank:
#     #     if curr_target.startswith(word) and len(word) > len(longest_prefix):
#     #       longest_prefix = word

#     #   if longest_prefix == '':
#     #     return float('inf')

#     #   new_idx = idx + len(longest_prefix)

#     #   return 1 + self.shortestWayHelper(wordBank, target, new_idx)

#     def wordBank(self, source):
#       if source == '':
#         return ['']

#       without_first = self.wordBank(source[1:])
#       with_first = [*without_first]
#       first = source[0]
#       for suffix in without_first:
#         with_first.append(first + suffix)

#       return with_first

#           # def shortestWay(self, source: str, target: str, idx = 0) -> int:
#     #   memo = {}
#     #   word_bank = self.wordBank(source)
#     #   word_bank.remove('')
#     #   output = self.shortestWayHelper(word_bank, target, 0, memo)

#     #   return -1 if output == float('inf') else output


#     def shortestWayHelper(self, word_bank, target: str, idx, memo):
#         if idx in memo:
#           return memo[idx]

#         if idx >= len(target):
#           return 0

#         curr_target = target[idx:]
        
#         min_path = float('inf')

#         for word in word_bank:
#           if curr_target.startswith(word):
#             new_idx = idx + len(word)
#             output = self.shortestWayHelper(word_bank, target, new_idx, memo)
#             min_path = min(min_path, output)
        
#         memo[idx] = 1 + min_path
#         return memo[idx]


# # 'potaot'.startswith('')




# # adec
# # a d d d e c

# # src = abc, target: ac



# # test = Solution()

# 'abc'
# 'ca'


# https://www.programiz.com/python-programming/methods/string/find
class Solution:
    def shortestWay(self, source: str, target: str, idx = 0) -> int:
      output = self.shortestWayHelper(source, target, 0)
      return -1 if output == float('inf') else output

    def shortestWayHelper(self, source, target, idx):
      if idx >= len(target):
        return 0
    
      last_source = -1
      greatest_i = -1

      for i in range(idx, len(target)):
        if last_source != -1:
          curr_source = source.find(target[i], last_source + 1)
        else:
          curr_source = source.find(target[i])
        if curr_source > last_source:
          last_source = curr_source
          greatest_i = i
        else:
          break

      if greatest_i == -1:
        return float('inf')

      return 1 + self.shortestWayHelper(source, target, greatest_i + 1)

s = Solution()


#       
# src: baab  , target: ab

# print(s.shortestWay('a', 'a'))
# print(s.shortestWay('abc', 'abcbc'))
print(s.shortestWay('aa', 'aa'))



# "abc"
# "abcbc"