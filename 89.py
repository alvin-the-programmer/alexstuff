# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
      ptr = head
        ktail = None
        new_head = None
        
        while ptr:
            count = 0
            ptr = head
            while count < k and ptr:
                ptr = ptr.next
                count += 1
                
            if count == k:
                rev_head = self.reverse(head, k)
                
                if not new_head:
                    new_head = rev_head
                    
                if ktail:
                    ktail.next = rev_head
                    
            ktail = head
            head = ptr
        
        if ktail:
            ktail.next = head
            
        return new_head if new_head else head
        
        
    def reverse(self, head, k):
        new_head, curr = None, head
        while k:
            temp = curr.next
            curr.next = new_head
            new_head = curr
            curr = temp
            k -= 1
            
        return new_head



    #     linked_list = self.convert_to_list(head)
    #     curr_sum = 0
        
    #     new_list = []
    
    #     count = 0
    #     while count < (len(linked_list) // k) :
    #         portion = linked_list[curr_sum:curr_sum + k]
    #         portion = portion[::-1]
    #         new_list += portion
    #         curr_sum += k
    #         count += 1
            
    #     new_list += linked_list[curr_sum:]
        
    #     return self.convert_to_linked_list(new_list)
        
    # def convert_to_linked_list(self, arr):
    #     if not arr:
    #         return None
    #     first = arr[0]
    #     curr_node = ListNode(first.val)
        
    #     curr_node.next = self.convert_to_linked_list(arr[1:])
        
    #     return curr_node

    # def convert_to_list(self, curr):
    #     if curr is None:
    #         return []
        
    #     return [curr] + self.convert_to_list(curr.next)


# https://leetcode.com/problems/symmetric-tree/solution/

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
      if not root:
        return False
      return self.isSymmetricHelper(root.left, root.right)
      
    def isSymmetricHelper(self, root1, root2):
      if root1 is None and root2 is None:
        return True
      if root1 is None or root2 is None:
        return False

      if root1.val != root2.val:
        return False

      return self.isSymmetricHelper(root1.left, root2.right) and self.isSymmetricHelper(root1.right, root2.left)


# https://leetcode.com/problems/find-median-from-data-stream/

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class MedianFinder:
    def __init__(self):
      """
      initialize your data structure here.
      """
      self.head = Node(None)
      self.count = 0

    def addNum(self, num: int) -> None:
      curr = self.head.next
      prev = self.head
      self.count += 1
      while curr:
        if curr.val > num:
          new_node = Node(num)
          prev.next = new_node
          new_node.next = curr
          return
        prev = curr
        curr = curr.next
      prev.next = Node(num)

    def findMedian(self) -> float:
      middle_idx = self.count // 2
      curr = self.head.next
      prev = self.head
      while middle_idx:
        middle_idx -= 1
        prev = curr
        curr = curr.next
      if self.count % 2 == 0:
        return (prev.val + curr.val) / 2
      else:
        return curr.val


        # [0 1 2 3 4]
     



# [A B C E F ]
#        3
# insert(D)

# len(dicti) / 2

# {
#   0 : Node(A)
#   1 : Node(B)
#   2 : Node(C)
#   3 : Node(D)
#   4: Node(E)
# }
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()