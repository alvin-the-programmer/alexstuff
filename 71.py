def canSum(target, nums):
  if target == 0:
    return True

  if target < 0:
    return False

  for num in nums:
    if canSum(target - num, nums) == True:
      return True
  return False


print(canSum(5, [5, 4, 3, 7]))
print(canSum(2, [5, 4, 3, 7]))
print(canSum(10, [5, 4, 3, 7]))


                #         5, [5, 4, 3, 7]
                #    5/     4/          \3       \7
                #  0        1            2        -2 
