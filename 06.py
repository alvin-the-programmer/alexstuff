# stacks
#    when you need a "history"

# Write a function, `is_balanced_parens` that takes in a string. The string will containing alphabetic characters
# and parens (, ). You fn should return a bool indicating whether or not the parentheses
# are valid in the string.

# Time: O(n)
# Space: O(n)
def is_balanced_parens(string):
    stack = []
    for letter in string:
        if letter == '(':
            stack.append('(')
        if letter == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

# print(is_balanced_parens('(alvin)')) # True
# print(is_balanced_parens('alex()')) # True
# print(is_balanced_parens('alex()()')) # True
# print(is_balanced_parens('(alex()())')) # True
# print(is_balanced_parens('(alex') )# False
# print(is_balanced_parens('(a)lex)') )# False
# print(is_balanced_parens(')alex()') )# False
# https://awwapp.com/b/uaas8iaude4fv/f

# s = "abcdefghij"

# print(s[::-2])

# for i in range(len(s) - 1 , -1, -1):
#     print(i)
#     print(s[i])

# Write a function, `is_balanced` that takes in a string. The string will containing alphabetic characters
# and parens ((,)), brackets ([]), braces ({}). You fn should return a bool indicating whether or not the matching chars
# are valid in the string.

# is_balanced('({[a}]s)') False
# is_balanced('({dfsdffdfd)') False
# is_balanced('(){s}a[l]x') True

