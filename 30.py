# https://leetcode.com/problems/course-schedule-ii/
# 2
# [1,0]

# out =
# 0 : [1]
# 1: []

# in =
# 0: []
# 1: [0]
# 1, []

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out_graph = self.outdegreeGraph(numCourses, prerequisites)  # O(n^2)
        in_graph = self.indegreeGraph(numCourses, prerequisites)  # O(n^2)

        course_order = []
        visited = set()

        progress = True
        while progress:  # O(n)
            progress = False

            for course in range(numCourses):  # O(n)
                # if the course has no parents AND i have not taken this
                if not in_graph[course] and course not in visited:
                    course_order.append(course)
                    visited.add(course)
                    progress = True
                    for after_course in out_graph[course]:  # O(n)
                        if course in in_graph[after_course]:
                            in_graph[after_course].remove(course)

        if len(course_order) != numCourses:
            return []

        return course_order

    def outdegreeGraph(self, numCourses, prerequisites):
        graph = {}

        for i in range(numCourses):
            graph[i] = set()

        for prereq in prerequisites:
            dest = prereq[0]
            source = prereq[1]

            graph[source].add(dest)

        return graph

    def indegreeGraph(self, numCourses, prerequisites):
        graph = {}

        for i in range(numCourses):
            graph[i] = set()

        for prereq in prerequisites:
            dest = prereq[0]
            source = prereq[1]

            graph[dest].add(source)

        return graph


test = Solution()
print(test.findOrder(1, []))
