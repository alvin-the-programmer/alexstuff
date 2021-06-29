# https://leetcode.com/problems/course-schedule/submissions/
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         inGraph = self.buildInGraph(numCourses, prerequisites)
#         visited = set()
#         progress = True

#         while progress:
#             progress = False
#             for node in inGraph:
#                 if not inGraph[node] and node not in visited:  # node has no parents
#                     for otherNode in inGraph:
#                         if node in inGraph[otherNode]:
#                             inGraph[otherNode].remove(node)
#                     visited.add(node)
#                     progress = True

#         if len(visited) == numCourses:
#             return True
#         else:
#             return False

#     def buildInGraph(self, numCourses, prereqs):
#         graph = {}

#         for i in range(numCourses):
#             graph[i] = set()

#         for prereq in prereqs:
#             last, first = prereq
#             graph[last].add(first)

#         return graph

# # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right


# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         roots = self.traverse(root)

#         if roots:
#             roots.pop(0)

#         curr = root
#         for node in roots:
#             curr.right = node
#             curr.left = None
#             curr = curr.right

#     def traverse(self, root):
#         if root is None:
#             return []

#         left = self.traverse(root.left)
#         right = self.traverse(root.right)

#         return [root] + left + right


def subsets(elements):
    if not elements:
        return [[]]

    output = subsets(elements[1:])
    newOutput = []
    for arr in output:
        newArr = arr[::]
        newArr.append(elements[0])
        newOutput.append(newArr)
        newOutput.append(arr)
    return newOutput


print(subsets(['a', 'b', 'c']))
