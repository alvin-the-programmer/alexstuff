# 10^12 = 8 * 4
# x^1 x^2 x^4 x^8 x^16 x^32 x^n
# 2^0, 2^1, 2^2, 2^3
# n = 10
class Solution:
    def myPow(self, x: float, n: int) -> float:
      powers = [] # [1, 2, 4, 8]

      power = 1
      while power <= abs(n):
        powers.append(power)
        power *= 2
      
      remainder = abs(n)
      idx = len(powers) - 1
      used = []
      while remainder:
        if powers[idx] <= remainder:
          remainder -= powers[idx]
          used.append(powers[idx])
        idx -= 1

      powers_of_x = {} 
      qty = x
      
      for power in powers:
        powers_of_x[power] = qty
        qty *= qty
      
      final_ans = 1
      for u in used:
        final_ans *= powers_of_x[u]

      if n < 0:
        return 1 / final_ans
      else:
        return final_ans


s = Solution()
print(s.myPow(2, 5))
print(s.myPow(2, 3))
print(s.myPow(2, -2))




"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
      curr = head
      stack = []
      prev = None
      while curr or stack:
        if curr is None:
          curr = stack.pop()
          prev.next = curr
          curr.prev = prev

        prev = curr
        if curr.child is not None:
          if curr.next is not None:
            stack.append(curr.next)
          curr.next = curr.child
          curr.child.prev = curr
          temp = curr.child
          curr.child = None
          curr = temp
        else:
          curr = curr.next

      return head