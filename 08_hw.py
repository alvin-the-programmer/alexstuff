# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head != None:
            second_to_last_nodes = self.convert_ll_to_list(head.next)
        else: # incase the linked list is empty
            return

        curr_node = head
        counter = 0
        while len(second_to_last_nodes) > 0:
            if counter % 2 == 0:
                curr_node.next = second_to_last_nodes.pop()
            else:
                curr_node.next = second_to_last_nodes.pop(0)   
                
            if len(second_to_last_nodes) == 0:
                # when we are done assigning our nodes, we must ENSURE our last node points to NOTHING in case it used to point to another NODE to avoid "cycle" errors
                curr_node.next.next = None 
                curr_node = None
            else:
                curr_node = curr_node.next
            counter += 1
    
    def convert_ll_to_list(self, head):
        nodes = []
        while head != None:
            nodes.append(head)
            head = head.next
        return nodes