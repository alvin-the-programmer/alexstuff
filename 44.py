# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        currL1 = l1
        currL2 = l2
        head = l1 if l1.val < l2.val else l2
        
        if head == l1:
            currL1 = currL1.next
        else:
            currL2 = currL2.next
        
        currHead = head
        while currL1 is not None and currL2 is not None:
            if currL1.val <= currL2.val:
                currHead.next = currL1
                currL1 = currL1.next
            else:
                currHead.next = currL2
                currL2 = currL2.next
            currHead = currHead.next
        
        currHead.next = currL1 if currL2 is None else currL2
        
        return head