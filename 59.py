# https://leetcode.com/problems/task-scheduler/

from typing import List
from collections import deque, Counter


# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         task_count = Counter(tasks)
#         history = deque()
#         history_task_count = {task: 0 for task in task_count}
#         turns = 0
#         while any(task_count[task] > 0 for task in task_count):
#             order = task_count.most_common()                      #O(T log T)
#             task_taken = False
#             for choice in order:
#                 task, count = choice
#                 if history_task_count[task] == 0:
#                     history.append(task)
#                     history_task_count[task] = 1
#                     task_count[task] -= 1
#                     task_taken = True
#                     break

#             if not task_taken:
#                 history.append(None)

#             if len(history) > n:
#                 oldest_task = history.popleft()
#                 if oldest_task is not None:
#                     history_task_count[oldest_task] -= 1
#             turns += 1

# #         return turns


# # tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G", "B"]
# # c = Counter(tasks)
# # print(c.most_common(3))
# # print(c.most_common())
# # print(c)


# s = Solution()
# print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))  # 8
# print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))  # 6
# print(s.leastInterval(tasks=["A", "A", "A", "A", "A",
#                              "A", "B", "C", "D", "E", "F", "G"], n=2))  # 16


stuff = [
    "potato",
    "applejacks",
    "zebra"
]

new_stuff = sorted(stuff, key=lambda s: len(s), reverse=True)
print(new_stuff)
