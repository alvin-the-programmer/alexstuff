class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        permutations = self.find_all_permutations(n, k)

        all_paths = []
        for node in permutations:
            all_paths += self.df_traversal(permutations, node, set())

        final_strs = []
        for path in all_paths:
            final_strs.append(self.compress_str(path))

        return min(final_strs, key=len)
    # 012345879

    def df_traversal(self, nodes, curr_node, visited):
        if curr_node in visited:
            return []

        visited.add(curr_node)

        if len(visited) == len(nodes):
            return [[curr_node]]

        output = []
        for neighbor in nodes:
            output += self.df_traversal(nodes, neighbor, set(visited))

        for path in output:
            path.append(curr_node)

        return output

    def find_all_permutations(self, n, k):
        if n == 0:
            return [""]

        output = []
        for i in range(k):
            subs = self.find_all_permutations(n - 1, k)
            for sub in subs:
                output.append(sub + str(i))

        return output

    def compress_str(self, path):
        output = path[0]

        for choice in path[1:]:
            for idx in range(len(choice), -1, -1):
                if output.endswith(choice[:idx]):
                    output += choice[idx:]
                    break

        return output


# ['11', '10', '01x', '00']

# 001101

# [[], [], []]

# [ '001', '010 , '100' ]
# '00100'


# debruijn sequence
test = Solution()
# print(test.find_all_permutations(2, 2))
print(test.crackSafe(1, 10))
# print(test.compress_str(['001', '010', '100']))
# '00100'


# [ '001', '010 , '100' ]
# '00100
# [100, 001]
# [1001]

# print(test.crackSafe(2, 2))


# "00" "01" "10" "11"

# n = 2
# k = 3 (0 1 2)

# permutation
# 01
# 10
# Example 2
# Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.

# 00
# 11
# 01
# 10

# """     "00" "01" "10" "11"
#             n=2, k=2
#           0/        \1
#    "0" n=1 "1"       n=1
#     0/   \1         0/  \1
#   n=0     n=0
#   ""
# """


# "00"  "01" "10" "11"

# 00  -  01
#  |     |  \
#  |    11 - 10
#  |          |
#  -     -    -

# visited
# 00110

# k = 2
# n = 3

# 000 001 010 011 100 101 110 111
