from collections import deque 
# import collections

# my_double_ended_queue = collections.deque([1,3,4,5])
# my_double_ended_queue.append(6)
# my_double_ended_queue.appendleft(7)
# my_double_ended_queue.pop()
# my_double_ended_queue.popleft()

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head == None:
            return

        second_to_last_nodes = deque(self.convert_ll_to_list(head.next))
        
        curr_node = head
        counter = 0
        while len(second_to_last_nodes) > 0:
            if counter % 2 == 0:
                curr_node.next = second_to_last_nodes.pop()
            else:
                curr_node.next = second_to_last_nodes.popleft()   
            curr_node = curr_node.next
            counter += 1
        # when we are done assigning our nodes, we must ENSURE our last node points to NOTHING in case it used to point to another NODE to avoid "cycle" errors
        curr_node.next = None 
        

    # def convert_ll_to_list(self, head):
    #     nodes = deque([])
    #     while head != None:
    #         nodes.append(head)
    #         head = head.next
    #     return nodes


    def convert_ll_to_list(self, head):
        if head is None:
            return []
        remaining_list = self.convert_ll_to_list(head.next)
        return  [ head, *remaining_list ]

    # recursive


# 856. score of parentheses
# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Example:
# Input: "( () ( () ) )"
# Output: 6
# 
# ((((((()))))))
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for curr in S:
            if curr == '(':
                stack.append(curr)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    temp = stack.pop()
                    stack.pop()
                    stack.append(temp * 2)

            if len(stack) > 1 and type(stack[-1]) == int and type(stack[-2]) == int:
                temp = stack.pop()
                stack[-1] += temp
          
        return stack[0]
            
    # ['(', 1, '(', 1]
    # ['(', 4]

    # ['(', 2]