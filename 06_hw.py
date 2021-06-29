# Write a function, `is_balanced` that takes in a string. The string will containing alphabetic characters
# and parens ((,)), brackets ([]), braces ({}). You fn should return a bool indicating whether or not the matching chars
# are valid in the string.

# '({[a]}s)'
        # c

# stack = [ ]

def is_balanced(string):
    stack = []
    closers = [')', ']', '}']
    stack_item = { '(': ')', '{': '}', '[': ']'}
    for letter in string:
        if letter in stack_item:
            stack.append(stack_item[letter])
        
        if letter in closers:
            if len(stack) == 0:
                return False
            elif letter == stack[-1]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

print(is_balanced('({[a]}s)')) # True
print(is_balanced('({dfsdffdfd)')) # False
print(is_balanced('(){s}a[l]x'))  # True
print(is_balanced('(potato'))  # False



