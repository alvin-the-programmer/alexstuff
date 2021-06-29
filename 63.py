# n = len(intervals)
# x = max_num of interval

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# output = [[1,6],[8,10],[15,18]]


# [[1, 4], [5, 6]]


#  0 1 2 3 4 5 6
# [0 1 1 1 1 2 2 ]


# [[1, 4], [4, 6]]
#  0 1 2 3 4 5 6
# [0 1 1 1 1 1 1 ]


def merge(intervals):
    intervals.sort(key=lambda interval: (interval[0], interval[1]))
    flat_list = sum(intervals, [])
    max_num = max(flat_list)
    ranges = [0] * (max_num + 1)

    count = 0
    for interval in intervals:
        start, end = interval
        if ranges[start] == 0:
            count += 1
            identifier = count
        else:
            identifier = ranges[start]
        for i in range(start, end + 1):
            ranges[i] = identifier
    # print(ranges)
    output = []
    start = 0
    while start < len(ranges):
        if ranges[start] != 0:
            for end in range(start, len(ranges)):
                if ranges[end] != ranges[start]:
                    output.append([start, end - 1])
                    start = end
                    break
                elif end == len(ranges) - 1:
                    output.append([start, end])
                    start = end + 1
        else:
            start += 1

    return output


stuff = [[4, 10], [2, 5], [2, 3]]
# stuff = [ [2, 3] [2, 5], [4, 10] ]
stuff.sort(key=lambda interval: (interval[0], interval[1]))  # sort key lambda
print(stuff)


# [ o o x x x x x  x x x x ]
#                        s
#                        e                s
# print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [5, 6]]))
# print(merge([[1, 4], [4, 6]]))
