class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counts = []
        
        for idx in range(len(tree)):
            counts.append(self.find_num_fruits(tree[idx:]))
        print(counts)
        return max(counts)
        
    def find_num_fruits(self, pickings):
        trees = {}
        count = 0
        
        for fruit in pickings:
            if fruit not in trees and len(trees) == 2:
                break
            
            if fruit not in trees and len(trees) < 2:
                trees[fruit] = 0    
            
            if fruit in trees:
                trees[fruit] += 1
                count += 1
    
        return count

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counts = []
        idx = 0
        while idx < len(tree):
            result = self.find_num_fruits(tree[idx:])
            index, count = result
            idx = idx + index
            counts.append(count)
            
        return max(counts)
        
    def find_num_fruits(self, pickings):
        trees = {}
        count = 0
        index = 0
        
        for idx, fruit in enumerate(pickings):
            if fruit not in trees and len(trees) == 2:
                break
            
            if fruit not in trees and len(trees) < 2:
                if len(trees) == 1:
                    index = idx
                trees[fruit] = 0 
            
            if fruit in trees:
                trees[fruit] += 1
                count += 1
    
        return (index, count)


  def totalFruit(self, tree):
        count, i = {}, 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        return j - i + 1

class Solution(object):
    def totalFruit(self, tree):
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans

        # https://leetcode.com/problems/course-schedule-ii/