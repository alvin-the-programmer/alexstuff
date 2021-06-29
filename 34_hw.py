# https://leetcode.com/problems/satisfiability-of-equality-equations/submissions/
class Solution:
    def equationsPossible(self, edges: List[str]) -> bool:
        comp = {}
        for edge in edges:
            nodeA = edge[0]
            nodeB = edge[3]
            comp[nodeA] = nodeA
            comp[nodeB] = nodeB

        for edge in edges: # O(n^2)
            nodeA = edge[0]
            nodeB = edge[3]
            eq = edge[1]
            if eq == '=':
                self.union(comp, nodeA, nodeB) # O(n)

        for edge in edges: #O(n^2)
            nodeA = edge[0]
            nodeB = edge[3]
            eq = edge[1]
            if eq == '!':
                if self.find(comp, nodeA) == self.find(comp, nodeB): #O(n)
                    return False
        return True

    def find(self, comp, teammate):
        if comp[teammate] == teammate:
            return teammate
        return self.find(comp, comp[teammate])

    def union(self, comp, nodeA, nodeB):
        parent_nodeA = self.find(comp, nodeA)
        parent_nodeB = self.find(comp, nodeB)

        comp[parent_nodeA] = parent_nodeB

# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n):
        memo = {}
        return self.numTreesHelper(n, memo)

    def numTreesHelper(self, n, memo): # n = 10
        if n in memo:
            return memo[n]

        if n == 0 or n == 1:
            return 1
        
        total = 0
        for i in range(1, n + 1): # i = 3
            nodes_in_left = i - 1 # 2
            nodes_in_right = n - i # 7
            # count = nodes_in_left * nodes_in_right
            count = self.numTreesHelper(nodes_in_left, memo) * self.numTreesHelper(nodes_in_right, memo)
            total += count
        
        memo[n] = total
        return memo[n]
        
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/

            nodes_in_right = n - i # 7
            count = nodes_in_left * nodes_in_right
            count = self.numTreesHelper(nodes_in_left, memo) * self.numTreesHelper(nodes_in_right, memo)
            total += count
        
        memo[n] = total
        return memo[n]
        
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/

            nodes_in_right = n - i # 7
            count = nodes_in_left * nodes_in_right
            count = self.numTreesHelper(nodes_in_left, memo) * self.numTreesHelper(nodes_in_right, memo)
            total += count
        
        memo[n] = total
        return memo[n]
        
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/

            nodes_in_right = n - i # 7
            count = nodes_in_left * nodes_in_right
            count = self.numTreesHelper(nodes_in_left, memo) * self.numTreesHelper(nodes_in_right, memo)
            total += count
        
        memo[n] = total
        return memo[n]
        
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/

            nodes_in_right = n - i # 7
            count = nodes_in_left * nodes_in_right
            count = self.numTreesHelper(nodes_in_left, memo) * self.numTreesHelper(nodes_in_right, memo)
            total += count
        
        memo[n] = total
        return memo[n]
        
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/


# https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://awwapp.com/b/uyidsx3ckcxjf/


# https://awwapp.com/b/uyidsx3ckcxjf/



