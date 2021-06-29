# Definition for singly-linked list.
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        list_of_nodes = []
        curr = head
        while curr != None:
            list_of_nodes.append(curr.val)
            curr = curr.next
       
        next_greatest_index = []
        final_output = []
        for i in range(len(list_of_nodes) - 1, -1, -1):
            curr = list_of_nodes[i]
            if len(next_greatest_index) == 0:
                final_output.append(0)
                next_greatest_index.append(i)
                continue
            
            top_of_stack = list_of_nodes[next_greatest_index[-1]]
            
            if top_of_stack > curr:
                final_output.insert(0, top_of_stack)
                next_greatest_index.append(i)
            else:
                while len(next_greatest_index) != 0 and top_of_stack <= curr:
                    next_greatest_index.pop()
                val = 0 if len(next_greatest_index) == 0 else top_of_stack
                final_output.insert(0, val)
                next_greatest_index.append(i)
                
#         return final_output
# [2,1,5]
# [0,5,0]
# [5,5,0]
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        list_of_nodes = []
        curr = head
        while curr != None:
            list_of_nodes.append(curr.val)
            curr = curr.next
       
        next_greatests = []
        final_output = []
        for i in range(len(list_of_nodes) - 1, -1, -1):
            curr = list_of_nodes[i]
  
            while len(next_greatests) != 0 and next_greatests[-1] <= curr:
                next_greatests.pop()
            val = 0 if len(next_greatests) == 0 else next_greatests[-1]
            final_output.append(val)
            next_greatests.append(curr)
                
        return final_output[::-1]
[5,4,3,2,1]

s = Solution()
a = ListNode(2)
b = ListNode(1)
c = ListNode(5)
a.next = b
b.next = c
print(s.nextLargerNodes(a))