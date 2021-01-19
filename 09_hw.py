# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# a -> b -> c
# 3

# b -> c
class Solution: # m = # nodes in list
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_list = self.convert_ll_to_list(head)
      
        if n == len(new_list):
            return None if n == 1 else new_list[-n+1]
        front = new_list[-n-1]
        back = None if n == 1 else new_list[-n+1]
        front.next = back
        
        return head
    
#     this is not PURE recursion because when the recursive calls finally "return", new_list already has all of its values. how can you adjust this?
    # def convert_ll_to_list(self, head, new_list = []):
    #     if head == None:
    #         return new_list
    #     new_list.append(head)
    #     return self.convert_ll_to_list(head.next, new_list)
    
    def convert_ll_to_list(self, head):
        new_list = []
        while head != None:
            new_list.append(head)
            head = head.next
        return new_list


# ALTERNNATE SOLUTION
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        second = dummy
        
        # bring first ptr to the end
        for i in range(0, n + 1):
            first = first.next
        
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next