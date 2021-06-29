# https://leetcode.com/problems/keys-and-rooms/
# https://awwapp.com/b/uufihtd4um9rv/

# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         visited = set()
#         self.canVisitAllRoomsHelper(rooms, 0, visited)
#         return len(visited) == len(rooms)

#     def canVisitAllRoomsHelper(self, rooms, curr_room, visited):
#         if curr_room in visited:
#             return
#         visited.add(curr_room)
#         for neighbor_room in rooms[curr_room]:
#             self.canVisitAllRoomsHelper(rooms, neighbor_room, visited)

from typing import List
edges = [
    (0, 1),
    (0, 2),
    (2, 3),
    (3, 1)
]

# def build_adj_list(edge_list):
#     adj_list = {}
#     for edge in edge_list:
#         src, dest = edge
#         if src in adj_list:
#             adj_list[src].append(dest)
#         else:
#             adj_list[src] = [dest]
#             if dest not in adj_list:
#                 adj_list[dest] = []
#     return adj_list


def build_adj_list(edge_list):
    adj_list = {}
    for edge in edge_list:
        src, dest = edge

        if src not in adj_list:
            adj_list[src] = []

        if dest not in adj_list:
            adj_list[dest] = []

        adj_list[src].append(dest)

    return adj_list


# print(build_adj_list(edges))
# {
#   0: [1, 2],
#   1: []
#   2: [3],
#   3: [1]
# }
# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        outDegree = {}
        inDegree = {}

        for i in range(1, N + 1):  # n
            outDegree[i] = set()
            inDegree[i] = set()

        for subArr in trust:  # k
            source, dest = subArr
            outDegree[source].add(dest)
            inDegree[dest].add(source)

        for num in range(1, N + 1):  # n
            if len(outDegree[num]) == 0:
                potential_judge = num
                if len(inDegree[potential_judge]) == N - 1:
                    return potential_judge
        return -1


#     find the node that has no source number vs. N
#
s = Solution()
print(s.findJudge(3, [[1, 3], [2, 3]]))
