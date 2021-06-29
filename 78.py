def isValidParentheses(s):
	count = 0
	for letter in s:
		if letter == "(":
			count += 1
		elif letter == ")":
			count -= 1
		if count < 0:
			return False
	return count == 0

def getPossibilities(s):
  if not s:
    return [""]

  first = s[0]

  possibilities_wo_first = getPossibilities(s[1:])
  possibilities_w_first = []
  for poss in possibilities_wo_first:
    possibilities_w_first.append(first + poss)

  return possibilities_w_first + possibilities_wo_first

class Solution:
  def removeInvalidParentheses(self, s: str) -> str:
    possibilities = set(getPossibilities(s))

    output = []
    max_len = float('-inf')

    for poss in possibilities:
      if isValidParentheses(poss) == True:
        output.append(poss)
        if len(poss) > max_len:
          max_len = len(poss)
		
    return [ poss for poss in output if len(poss) == max_len ]

# ()())()

# getPossibilities('()(')


#               ''
#           /        \
# (
#         ''              (
#       /    \           /  \
# )
#     ''       )        (      ()
#     / \      / \      / \      /\
# ( ''    (   )   )(   (   ((   ()  ()(
 

# [
#   '',

# ]

# abc

# https://leetcode.com/problems/remove-invalid-parentheses/

# "(a)())()"
# Output
# ["(a()()","()()()","(())()"]
# Expected
# ["(a())()","(a)()()"]



class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        left = 0
        right = 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:

            # Simply record the left one.
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it.
                right = right + 1 if left == 0 else right

                # Decrement count of left parentheses because we have found a right
                # which CAN be a matching one for a left.
                left = left - 1 if left > 0 else left

        result = {}
        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:

                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])    

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # Pop for backtracking.
                expr.pop()                 

        # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, left, right, [])     
        return list(result.keys())




# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# [8,8,8,8,8,8,8]


#                               [5,7,7,8,8,10],
#                                     /   \
  
# # target = 8
# #
# #  [5,7,7,7,7,8,8,8,10] 
# #  lo       m       hi

# # target = 8
# #  [5,7,7,7,7,7,8,8,10] 
# #            lo m hi




# lo, mid, hi
# target = 8
# [8,8,8,8,8,8,10,10]
# l          m h

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
        
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        # 7 7 7 7 8 8 8 8 10 10 10
				          m 
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            
            if nums[mid] == target:
                
                if isFirst:
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    end = mid - 1
                else:

                    if mid == end or nums[mid + 1] > target:
                        return mid
                    
                    begin = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1