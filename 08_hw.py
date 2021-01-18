# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 143. reorder list: my solution
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

# 856. score of parentheses
# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Example:
# Input: "( () ( () ) )"
# Output: 6
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for curr in S:
            if curr == '(':
                stack.append(curr)
            
            if stack[-1] == '(' and curr == ')':
                stack.pop()
                stack.append(1)
            elif type(stack[-1]) == int and curr == ')':
                temp = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp * 2)
                
            while len(stack) > 1 and type(stack[-1]) == int:
                temp = stack[-1]
                stack.pop()
                if type(stack[-1]) == int:
                    temp += stack[-1]
                    stack.pop()
                    stack.append(temp)
                else:
                    stack.append(temp)
                    break
        
        return stack[0]
            