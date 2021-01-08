# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
 def __init__(self, val):
  self.next = None
  self.val = val

# create a new list OR modify old ones
# start looking at the head of both lists
# sum their values + current value of carry
# check if it is over 9 at any point
    # if it is, make carry 1
    # ELSE make carry 0
# make recursive call to next nodes in list

def addTwoNumbers(l1_curr: Node, l2_curr: Node, l3_prev = None, carry = 0) -> Node:
    # return traverse(l1, l2)
    # base case, end of list and NO carry
    if carry == 0 and l1_curr == None and l2_curr == None:
        return l3_prev

    l1_val = 0 if l1_curr == None else l1_curr.val
    l2_val = 0 if l2_curr == None else l2_curr.val

    final_sum = l1_val + l2_val + carry
    if final_sum > 9:
        carry = 1
        final_sum -= 10
    else:
        carry = 0

    l3 = Node(final_sum)
    
    if l3_prev != None:
        l3_prev.next = l3

    # CLARIFY: why do we return l3 and not the recursive call?
    # I THINK its because we only want the HEAD of l3 back, not any of the other nodes, so we call the recursive call,
    #  and then when everything is finished bubbling up and returning, we are LEFT with the HEAD of list 3

    addTwoNumbers(l1_curr.next, l2_curr.next, l3, carry)
    return l3

# def traverse(l1_curr, l2_curr, l3_prev = None, carry = 0):
    # # base case, end of list and NO carry
    # if carry == 0 and l1_curr == None and l2_curr == None:
    #     return l3_prev

    # l1_val = 0 if l1_curr == None else l1_curr.val
    # l2_val = 0 if l2_curr == None else l2_curr.val

    # final_sum = l1_val + l2_val + carry
    # if final_sum > 9:
    #     carry = 1
    #     final_sum -= 10
    # else:
    #     carry = 0

    # l3 = Node(final_sum)
    
    # if l3_prev != None:
    #     l3_prev.next = l3

    # # CLARIFY: why do we return l3 and not the recursive call?
    # # I THINK its because we only want the HEAD of l3 back, not any of the other nodes, so we call the recursive call,
    # #  and then when everything is finished bubbling up and returning, we are LEFT with the HEAD of list 3

    # traverse(l1_curr.next, l2_curr.next, l3, carry)
    # return l3

def print_list(head):
    if head == None:
        return
    print(head.val)
    print_list(head.next)

# NO CARRIES
# l1 = Node(3)
# l1.next = Node(2)
# l1.next.next = Node(1)

# l2 = Node(1)
# l2.next = Node(2)
# l2.next.next = Node(3)

# WITH CARRIES
l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)

l2 = Node(3)
l2.next = Node(9)
l2.next.next = Node(1)

# DIFF LENGTHS
# l1 = Node(1)
# l1.next = Node(2)
# l1.next.next = Node(3)

# l2 = Node(3)
# l2.next = Node(9)
# l2.next.next = Node(1)
# l2.next.next.next = Node(1)

print_list(addTwoNumbers(l1, l2))

# examples
# list with no carries
# list with carries
# different lengths
# list with a carry after the list ends