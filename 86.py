# https://leetcode.com/problems/maximum-frequency-stack/solution/

from collections import defaultdict

class FreqStack:
    def __init__(self):
      self.freq = defaultdict(int)
      self.group = defaultdict(list)
      self.max_freq = 0

    def push(self, val: int) -> None:
      self.freq[val] += 1
      curr_freq = self.freq[val]
      self.group[curr_freq].append(val)

      if curr_freq > self.max_freq:
        self.max_freq = curr_freq

    def pop(self) -> int:
      greatest_group = self.group[self.max_freq]
      popped = greatest_group.pop()

      self.freq[popped] -= 1

      if len(greatest_group) == 0:
        self.max_freq -= 1

      return popped

freqStack = FreqStack()
freqStack.push(5); # The stack is [5]
freqStack.push(7); # The stack is [5,7]
freqStack.push(5); # The stack is [5,7,5]
freqStack.push(7); # The stack is [5,7,5,7]
freqStack.push(4); # The stack is [5,7,5,7,4]
freqStack.push(5); # The stack is [5,7,5,7,4,5]
freqStack.pop();   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].\


# ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
# [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]

# [4,0,9,3,4,2]
"""
# max_freq = 1
  # freq = {
      4: 2
      0: 1
      9: 1
      3: 1
      2: 1
  # } 

  # group = {
  #   1: [4, 0, 9, 3, 2]
      2: []
  # }

"""
# 1: [3,4]
# 2: []
# 3: [2]

  #  [5, 7 , 5, 7 , 4, 5]
  #                    x 
  

  # max_freq = 2
  
  # freq = {
  #   5: 2,
  #   7: 2,
  #   4: 1
  # } 

  # group = {
  #   1: [5, 7, 4]
  #   2: [5]
  #   3: []
  # }


# from collections import defaultdict


# int
# list
# tuple
# dict
# group = defaultdict(list)
# group[2].append('a')  
# group[2].append('a')  
# print(group)
# print(group[2])
