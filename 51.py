class Solution:
    def numPermsDISequence(self, S: str) -> int:
        arr = set()
        for i in range(len(S) + 1):
            arr.add(i)
        return self.numberPermsHelper(arr, S)

    def numberPermsHelper(self, arr, S, lastNum = None):
        if S == '' and not arr:
            return 1

        tSum = 0
        
        for num in arr:
            if lastNum is None:
                newSet = set(arr)
                newSet.remove(num)
                tSum += self.numberPermsHelper(newSet, S, num)
            else:
                if S[0] == 'D':
                    if num < lastNum:
                        newSet = set(arr)
                        newSet.remove(num)
                        print(arr)
                        tSum += self.numberPermsHelper(newSet, S[1:], num)
                elif S[0] == 'I':
                    if num > lastNum:
                        newSet = set(arr)
                        newSet.remove(num)
                        tSum += self.numberPermsHelper(newSet, S[1:], num)
        return tSum
	
class Solution:
  def numPermsDISequence(self, S: str) -> int:
    memo = {}
    nums = set( i for i in range(0, len(S) + 1) )
    total = 0
    for num in nums:
      next_nums = set(nums)
      next_nums.remove(num)
      total += self.recurse(S, next_nums, num, memo)

    return total

  def recurse(self, S, nums, last, memo):
    nums_sorted = tuple(sorted(list(nums)))

    key = (S, nums_sorted, last)

    if key in memo:

      return memo[key]

    if not nums:
      return 1

    first_char = S[0]
    rest_chars = S[1:]

    if first_char == 'D':
      total_ways = 0
      for num in nums:
        if num < last:
          next_nums = set(nums)
          next_nums.remove(num)
          total_ways += self.recurse(rest_chars, next_nums, num, memo)
      memo[key] = total_ways
      return total_ways
    else:
      total_ways = 0
      for num in nums:
        if num > last:
          next_nums = set(nums)
          next_nums.remove(num)
          total_ways += self.recurse(rest_chars, next_nums, num, memo)
      memo[key] = total_ways
      return total_ways


s = Solution()
print(s.numPermsDISequence('DID'))
# The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)

# helper({3, 2}, 'D')

# lastNum = None

# helper({2}, '', 3)     helper({3}, '', 2)


# asdasdasd


# [
#     'b->d', 'b->e'
# ]

# [
#     'c'
# ]


#    (a)
#   /  \
#  b    c 
# / \
#d  e        
