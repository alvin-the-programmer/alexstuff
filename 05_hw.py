# 445
# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        while l1 != None:
            list1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            list2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        l3_next = None
        
        while len(list1) != 0 or len(list2) != 0 or carry != 0:
            l1_val = list1.pop() if len(list1) != 0 else 0
            l2_val = list2.pop() if len(list2) != 0 else 0
       
            curr_sum = l1_val + l2_val + carry
            
            if curr_sum > 9:
                carry = 1
                curr_sum -= 10
            else:
                carry = 0
                
            l3_curr = ListNode(curr_sum)
            l3_curr.next = l3_next
            l3_next = l3_curr
            
        return l3_next