# https://leetcode.com/problems/trapping-rain-water

from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        left_max = 0
        for i in range(len(height)):
            left.append(left_max)
            if height[i] > left_max:
                left_max = height[i]

        right = deque([])
        right_max = 0
        for i in range(len(height) - 1, -1, -1):
            right.appendleft(right_max)
            if height[i] > right_max:
                right_max = height[i]
        
        water_sum = 0
        for i in range(len(height)):
            smallest_wall = min(left[i], right[i])
            water_unit = smallest_wall - height[i]

            if water_unit > 0:
                water_sum += water_unit
        
        return water_sum
        

"""
height = 
                   X
           X W W W X
       X W X X W X X
H = [0,1,0,2,1,0,1,3]
                   C
L = [0 0 1 1 2 2 2 2]
R = [3 3 3 3 3 3 3 0]
     0 0 1 0 1 2 1 0


"""


# https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        curr = head
        nodes = {
            id(head) : Node(head.val)
        }
        new_head = nodes[id(head)]

        while curr:
            if curr.next and id(curr.next) not in nodes:
                nodes[id(curr.next)] = Node(curr.next.val)
            if curr.random and id(curr.random) not in nodes:
                nodes[id(curr.random)] = Node(curr.random.val)
            nodes[id(curr)].next = nodes[id(curr.next)] if curr.next else None
            nodes[id(curr)].random = nodes[id(curr.random)] if curr.random else None
            curr = curr.next

        return new_head




# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         return copy_list_random_ptr(head)


# def copy_list_random_ptr(head):
#     copies = {}
#     tag_nodes(head)
#     return copy_helper(head, copies)

# def tag_nodes(head, idx = 0):
#   if head is None:
#     return

#   head.id = idx

#   tag_nodes(head.next, idx + 1)
#   return head

# def copy_helper(head, copies):
#     if head is None:
#         return None

#     new_root = copies[head.id] if head.id in copies else Node(head.val)
#     copies[head.id] = new_root

#     curr_random = head.random
#     if curr_random is not None:
#       new_random = copies[curr_random.id] if curr_random.id in copies else Node(curr_random.val)
#       copies[curr_random.id] = new_random
#       new_root.random = new_random

#     new_root.next = copy_helper(head.next, copies)
#     return new_root

"""
[[7,null],[13,0],[11,4],[10,2],[1,0]]

7 -next> 13
  -random> None 

13 -next> 11
   -random> 7

new_head = 7
{
    7: Node(7)
    13: Node(13)
    11: Node(11)
}

"""        