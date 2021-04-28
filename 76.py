# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# # input: [ 5, 2 ,3, 1 ]
# # output: 5 -> 2 -> 3 -> 1

# # [ 5, 2 ,3, 1 ]
# #         X  
# # [1]
# #   3 >1
# #   P

# def convert_to_linked_list(nums):
#   if not nums:
#     return None
  
#   prev = None

#   for i in range(len(nums) - 1, -1, -1):
#     curr_val = nums[i]
#     curr = Node(curr_val)
#     curr.next = prev
#     prev = curr

#   return prev


# def convert_to_linked_list(nums):
#   if not nums:
#     return None
  
#   dummy_head = Node(None)
#   tail = dummy_head

#   for val in nums:
#     tail.next = Node(val)
#     tail = tail.next

#   return dummy_head.next

# def print_ll(head):
#   curr = head
#   values = []
#   while curr:
#     values.append(str(curr.val))
#     curr = curr.next

#   return "".join(values)

# nums = [ 5, 2 ,3, 1 ]
# ll = convert_to_linked_list(nums)

# nums2 = [ 1 ]
# ll2 = convert_to_linked_list(nums2)

# nums3 = [ ]
# ll3 = convert_to_linked_list(nums3)

# print(print_ll(ll))
# print(print_ll(ll2))
# print(print_ll(ll3))



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

# Output:
# preorder: S L R
# inorder : L S R
#      3
#    /  \
#   9    20
#       / \
#     15   7

                  #       [3,9,20,15,7], [9,3,15,20,7]  Node(3) 
                  #           /                 \
                  # Node(9)[9],[9]         [20,15,7], [15, 20, 7] Node(20)   
                  #         / \                     /         \
                  #    [],[]   [],[]             [15],[15]      [7][7]


def build_tree(preorder, inorder):
  if not preorder and not inorder:
    return None

  first_val = preorder[0]
  curr = TreeNode(first_val)

  inorder_idx = inorder.index(first_val)
  left_inorder = inorder[:inorder_idx]
  right_inorder = inorder[inorder_idx + 1:]

  curr.left = build_tree(preorder[1:1 + len(left_inorder)], left_inorder)
  curr.right = build_tree(preorder[len(inorder) - len(right_inorder):], right_inorder)
  
  return curr


  # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/