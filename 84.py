arr = [2,5,3,8,10]
# ans = [2,8,10,5,3]

# Time: O(n log n)
# Space: O(1)

# arr.sort(key = lambda x : x % 2 == 1)

# evens = []
# odds = []
# O(n)
# O(n)

# O(n)
# O(1)

arr = [2,5,3,8,10]
        #  L      H
# [1,1,1]

def sort_by_evens(arr):
  lo, hi = 0, len(arr) - 1
  while lo < hi:
    while arr[lo] % 2 == 0 and lo <= len(arr) - 1:
      lo += 1

    while arr[hi] % 2 == 1 and hi >= 0:
      hi -= 1

    temp = arr[lo]
    arr[lo] = arr[hi]
    arr[hi] = temp

    lo += 1
    hi -= 1

  return arr

print(sort_by_evens(arr))
print(sort_by_evens([6, 6, 6,7,7,6,6,6,7,6,7,6,7,6]))


# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
          self.stack.append((val, val))
        else:
          last_min = self.stack[-1][1]
          if val < last_min:
            self.stack.append((val, val))
          else:
            self.stack.append((val, last_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


MinStack minStack = new MinStack();
minStack.push(-2);#
minStack.push(0); #
minStack.push(-3);
minStack.getMin(); #return -3
minStack.pop();
minStack.top();    #return 0
minStack.getMin(); #return -2


#   (v, m)
#  . 
# .
#   (0, -2)
#  (-2, -2)
# ______

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()