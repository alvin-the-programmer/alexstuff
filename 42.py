# https://awwapp.com/b/uqkrzszzianpj/
import math
l
class MaxHeap:
    def __init__(self):
        self.array = [float('inf')]

    def insert(self, val):
        self.array.append(val)
        self.sift_up(len(self.array) - 1)

    def sift_up(self, i):
        curr = self.array[i]
        parent = self.array[i // 2]
        if parent < curr:
            self.array[i // 2] = curr
            self.array[i] = parent
            self.sift_up(i // 2)

    def delete(self):
        if len(self.array) <= 1:
            return None

        first = self.array[1]
        last = self.array[len(self.array) - 1]
        self.array[len(self.array) - 1] = first
        self.array[1] = last
        output = self.array.pop()
        self.sift_down(1)
        return output

    def sift_down(self, i):
        if i > len(self.array) - 1:
            return
        
        curr = self.array[i]
        if i * 2 <= len(self.array) - 1:
            left = self.array[i * 2]
            right = self.array[i * 2 + 1] if i * 2 + 1 <= len(self.array) - 1 else float('-inf')
            
            pos = i * 2 if left > right else i * 2 + 1
            child = self.array[pos]
            if curr < child:
                self.array[i] = child
                self.array[pos] = curr
                self.sift_down(pos)

my_heap = MaxHeap()
my_heap.insert(10)
my_heap.insert(15)
my_heap.insert(12)
my_heap.insert(6)
my_heap.insert(40)
my_heap.insert(20)
my_heap.insert(39)
my_heap.insert(15)
# print(my_heap.array)
# print(my_heap.delete())
# print(my_heap.delete())
# print(my_heap.array)
# print(my_heap.delete())
# print(my_heap.delete())
# print(my_heap.delete())
# print(my_heap.delete())
# print(my_heap.delete())

# print(my_heap.delete())

# print(my_heap.array)

# print(my_heap.delete())
# print(my_heap.delete())


# delete 40
# delete 39

#               20
#       15           12
#   15     10     6          

#  [inf  10  15  12  6  40  20  39  15 ]
#    0   1   2   3   4   5   6  7   8

# https://docs.python.org/3/library/heapq.html

import heapq




stuff = [  
    (5, 'red'), 
    (2, 'brown'),
    (1, 'yellow'),
    (10, 'purple'),
    (5, 'blue'), 
    ]
heapq.heapify(stuff)
heapq.heappush(stuff, (0, 'orange'))
print(stuff)

# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dupe = []
        for num in nums:
            dupe.append(-num)
        
        heapq.heapify(dupe)

        for idx in range(k):
            output = heapq.heappop(dupe)

        return -output