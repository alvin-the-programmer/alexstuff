
# [1, 3, 7]

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nodes = []
        self.df_traversal(root, nodes, 0)
        return root

    def df_traversal(self, curr, nodes, level):
        if curr is None:
            return

        if level == len(nodes):
            nodes.append(curr)
            # create the level for the first time
        else:
            nodes[level].next = curr
            nodes[level] = curr

        left = self.df_traversal(curr.left, nodes, level + 1)
        right = self.df_traversal(curr.right, nodes, level + 1)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        prev = None
        prev_level = -1

        queue = [(root, 0)]
        while queue:

            node, curr_level = queue.pop(0)

            if curr_level == prev_level:
                node.next = prev

            prev = node
            prev_level = curr_level

            if node.right:
                queue.append((node.right, curr_level + 1))

            if node.left:
                queue.append((node.left, curr_level + 1))

        return root


def reverse_list(head, prev=None):
    if head is None:
        return prev

    next_node = head.next
    head.next = prev
    return reverse_list(next_node, head)


# a -> b -> (c) -> d -> e -> ((N))
# e -> d ->
