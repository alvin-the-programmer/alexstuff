# https://leetcode.com/problems/leaf-similar-trees/
# class Solution:
#     def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
#         return self.getLeafNodes(root1) == self.getLeafNodes(root2)
        
#     def getLeafNodes(self, root):
#         if root == None:
#             return []
#         if root.left == None and root.right == None:
#             return [root.val]
        
#         result = []
#         left_leaves = self.getLeafNodes(root.left)
#         for node in left_leaves:
#             result.append(node)

#         right_leaves = self.getLeafNodes(root.right)
#         for node in right_leaves:
#             result.append(node)

#         return result

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves_1 = []
        leaves_2 = []

        self.getLeafNodes(root1, leaves_1) 
        self.getLeafNodes(root2, leaves_2)
        return leaves_1 == leaves_2
        
    def getLeafNodes(self, root, leaves):
        if root == None:
            return 

        if root.left == None and root.right == None:
            leaves.append(root.val)
            return 
        
        self.getLeafNodes(root.left, leaves)
        self.getLeafNodes(root.right, leaves)




# https://awwapp.com/b/up6inmhsgv9te/
        
# https://leetcode.com/problems/satisfiability-of-equality-equations/

# create an adjacency list?
# object likeso:
# {
#   'a' : ['b', 'c'],
#   'b' : ['a'],
#   'c' : ['d', 'a'],
#   'd' : ['c']
# }
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = {}
        # make adjacency list
        for eq in equations:
            firstChar = eq[0]
            sign = eq[1]
            secondChar = eq[3]
            
            if firstChar not in graph:
                graph[firstChar] = []

            if secondChar not in graph:
                graph[secondChar] = []
            # we only care about '=='s for creating our graph
            if sign == '=':
                graph[firstChar].append(secondChar)
                graph[secondChar].append(firstChar)
        # go thru equations again only finding "!="s
        for eq in equations:
            firstChar = eq[0]
            sign = eq[1]
            secondChar = eq[3]

            if sign == '!':
                # edge case, 1st and 2nd char are same char
                # impossible, a != a must be False
                # if firstChar == secondChar:
                #     return False
                # new set needs to be created each time
                visited = set()
                if self.checkForEquality(firstChar, secondChar, index, visited) == True:
                    return False
        return True
                
    def checkForEquality(self, source, dest, index, visited):
        if source in visited:
            return False
        
        visited.add(source)
        
        if source == dest:
            return True
        
        nodesToCheck = index[source]
        for node in nodesToCheck:
            if self.checkForEquality(node, dest, index, visited) == True:
                return True
    
        return False



# time:
# n = # of equations in list
# O(n + n^2) = O(n^2)

# space:
# n = # of equations
# O(n^2 + n + n) = O(n^2)


# dest: d
# visited:
# "a", "b", 
# cfe(a)
# cfe(b)
# cfe(c)

#  {
#   'a' : ['b', 'c'],
#   'b' : ['a'],
#   'c' : ['d', 'a'],
#   'd' : ['c']
# }

# https://leetcode.com/problems/evaluate-division/