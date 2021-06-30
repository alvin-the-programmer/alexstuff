class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr = [0,0]
        direction = 0 # north
        deltas = [(0,1), (1,0), (0,-1), (-1,0)] # N E S W

        for _ in range(4):
            for step in instructions:
                if step == 'G':
                    x_add, y_add = deltas[direction]
                    curr[0] += x_add
                    curr[1] += y_add
                elif step == 'L':
                    direction -= 1
                    if direction == -1:
                        direction = 3
                elif step == 'R':
                    direction += 1
                    direction %= 4
            if curr == [0, 0]:
                return True
        return False



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.build_graph(isConnected)

        visited = set()
        provinces = 0
        for city in graph:
            if city not in visited:
                provinces += 1
                self.df_traversal(city, graph, visited)
        
        return provinces

    def df_traversal(self, city, graph, visited):
        if city in visited:
            return

        visited.add(city)
        neighbors = graph[city]

        for neighbor in neighbors:
            self.df_traversal(neighbor, graph, visited)

    def build_graph(self, isConnected):
        graph = {}
        for i in range(1, len(isConnected) + 1):
            graph[i] = set()
        
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                curr = isConnected[row][col]
                if curr == 1 and row != col:
                    graph[row + 1].add(col + 1)
        return graph
# n = # of cities
# time O(n^2 + n + n)
# space O(n^2 + n)
        #   1 2 3
        # 1[0,0,0],      2 - 1
        # 2[0,0,0],        3
        # 3[0,0,0]


# adj list space: O(e)
# adj matrx space: O(n^2)

# e <= n^2
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_list = []
        self.num_dict = {}
        
    def insert(self, val: int) -> bool:
        if val in self.num_dict:
            return False
        self.num_list.append(val)
        self.num_dict[val] = len(self.num_list) - 1
        return True

    # remove(3)
    def remove(self, val: int) -> bool:
        if val not in self.num_dict:
            return False
        idx = self.num_dict[val]
        original_end = self.num_list[-1]
        self.num_list[-1], self.num_list[idx] = self.num_list[idx], self.num_list[-1]
        self.num_dict[original_end] = idx
        self.num_list.pop()
        del self.num_dict[val]
        # self.num_dict.pop(val)
        return True

    def getRandom(self) -> int:
        return self.num_list[random.randint(0, len(self.num_list) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

Input: time = 
[60,60,60]
       ^  
curr = 60
compleement = 

total = 3
{
    0: 3
}






count = 3
[30,20,150,100,40]
               ^ 
{
    30: 2
    20 : 1
    40 : 1
}


# check if 'complement = 60 - (self % 60)' in hash
# add (self % 60) to hash


(a + b) % 60 == 0

a % 60 + b % 60 == 0
a % 60 = -(b%60)`


Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
"""
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        num_pairs = 0
        complement = 60 



from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        total_count = 0
        for t in time:
            print(count)
            print('current t', t)
            complement = (60 - t)  % 60
            print('complement', complement)
            total_count += count[complement]
            print('total_count', total_count)

            count[t % 60] += 1

        return total_count

[30,20,150,100,40]
               ^

total_count = 2
complement = 


{
 30 : 2
 20 : 1
 40: 1
}



defaultdict(<class 'int'>, {})
current t 30
complement 30
total_count 0

defaultdict(<class 'int'>, {30: 1})
current t 20
complement 40
total_count 0

defaultdict(<class 'int'>, {30: 1, 40: 0, 20: 1})
current t 150
complement 30
total_count 1

defaultdict(<class 'int'>, {30: 2, 40: 0, 20: 1})
current t 100
complement 20
total_count 2

defaultdict(<class 'int'>, {30: 2, 40: 1, 20: 1})
current t 40
complement 20
total_count 3