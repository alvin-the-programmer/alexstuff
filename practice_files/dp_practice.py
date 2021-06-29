def grid_traveler(x, y):
    memo = {}
    return grid_traveler_helper(x, y, memo)

def grid_traveler_helper(x, y, memo={}):
    key = str(x) + ',' + str(y)

    if key in memo:
        return memo[key]
    if x == 1 and y == 1:
        return 1
    if x == 0 or y == 0:
        return 0
    memo[key] = grid_traveler_helper(x - 1, y, memo) + grid_traveler_helper(x, y - 1, memo)
    return memo[key]

# print(grid_traveler(18, 18))

# what about the note about x, y == y, x? 

def can_sum(target_sum, numbers):
    memo = {}
    return can_sum_helper(target_sum, numbers, memo)

def can_sum_helper(target_sum, numbers, memo):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    
    for number in numbers:
        remainder = target_sum - number
        if can_sum_helper(remainder, numbers, memo) == True:
            memo[target_sum] = True

            return True

    memo[target_sum] = False
    return False
    
# print(can_sum(7, [2, 3]))

def can_construct(target, wordBank):
    return can_construct_helper(target, wordBank)

def can_construct_helper(target, wordBank):
    if target == "":
        return True
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct_helper(suffix, wordBank) == True:
                return True
            
    return False

wordBank = ["abc", "de", "def"]
print(can_construct("abcdef", wordBank))