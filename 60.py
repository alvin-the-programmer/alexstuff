# def reverseParentheses(s):
#     curr_s = s
#     while '(' in curr_s:
#         count_open = 0
#         start_idx = 0
#         end_idx = 0
#         removed = False
#         for idx, char in enumerate(s):
#             if char == '(' and removed == False:
#                 if count_open == 0:
#                     start_idx = idx
#                 count_open += 1
#             if char == ')' and removed == False:
#                 count_open -= 1
#                 if count_open == 0:
#                     end_idx = idx
#                     removed = True
#         right_side = curr_s[end_idx + 1:] if end_idx + 1 <= len(curr_s) else ''
#         curr_s = curr_s[:start_idx] + \
#             curr_s[start_idx + 1:end_idx:-1] + right_side
#         print(curr_s)

#     return curr_s


# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
def reverseParen(s):
    new_s = s
    while '(' in new_s:
        new_s = reverseFirstParen(new_s)
        print(new_s)
    return new_s


def reverseFirstParen(s):
    first_open = s.index('(')

    open_count = 1
    for i in range(first_open + 1, len(s)):
        curr_let = s[i]
        if curr_let == '(':
            open_count += 1

        if curr_let == ')':
            open_count -= 1

            if open_count == 0:
                target_region = s[first_open + 1:i][::-1]
                new_region = ""
                for char in target_region:
                    if char == '(':
                        new_region += ')'
                    elif char == ')':
                        new_region += '('
                    else:
                        new_region += char
                return s[:first_open] + new_region + s[i + 1:]


print(reverseParen("ta()usw((((a))))"))
# print(reverseParen('abc(x(yz)w)'))  # 'abcw(zy)x'
# print(reverseFirstParen('A(BCD)'))
