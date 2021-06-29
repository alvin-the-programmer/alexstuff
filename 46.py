# inp = [4,5,6,7,10,10,20,100,101]
#      lo                    hi
# time: O(logn)
# space: O(1)

# def bSearch(inp, target):
#     lo = 0 #
#     hi = len(inp) - 1 #

#     while lo <= hi:
#         middleIdx = (hi + lo) // 2
#         middleVal = inp[middleIdx]
#         if middleVal == target:
#             return True
#         elif middleVal < target:
#             lo = middleIdx + 1
#         else:
#             hi = middleIdx - 1

#     return False

#   i:  0 1 2 3 4 5 6
# arr: [a b c d e f g]
#         l     h  


# inp = [4,5,6,7,10,10,20,100,101]
# print(bSearch(inp, 6)) # t
# print(bSearch(inp, 7)) # t
# print(bSearch(inp, 101)) # t
# print(bSearch(inp, 102)) # f
# print(bSearch(inp, 103)) # f


# print(bSearch([2], 2)) # t
# print(bSearch([2], 3)) # f
# print(bSearch([2,3], 3)) # t


# Write fn that takes in a list
# The fn should return the element of the list that appears the most freq # times


# from collections import Counter
# def most_freq(elements):
  # freq = Counter(elements)
#   maxLetter = None
#   for letter in freq:
#       if maxLetter is None or freq[letter] > freq[maxLetter]:
#           maxLetter = letter
#   return maxLetter


# print(most_freq(['a', 'b', 'a' ,'b', 'c', 'c', 'c', 'c' 'a'])) # 'a'

# count_one = Counter(['a', 'a', 'a', 'b', 'b', 'c']);
# count_two = Counter(['b', 'a', 'a', 'd']);
# print(count_one);
# print(count_two);
# print(count_one + count_two)


# set

# write a fn that takes in an array of numbers and returns  a bool indc if there is at least 1 even number
# in the array

# def has_even(items):
#   for item in items:
#     if item is_even(item):
#       return True

#   return False


def has_even(items):
  return any( is_even(n) for item in items )
any
all
def is_even(n):
  return n % 2 == 0

