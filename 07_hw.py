# n = length of str
# time: O(N) -> i was thinking n^2 if by chance there were just a series of: 3[a]3[b]3[c]???
# space: O(N) -> we could potentially have n/x recursive consolidate calls on the CALL stack, but our list will always be "consolidated" to less than N values

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ""
        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                stack.append(int(num))
                num = ""
            elif char == ']':
                self.consolidate(stack)
            else:
                stack.append(char)
        return ''.join(stack)
        
    def consolidate(self, stack, group = ""):
        if type(stack[-1]) == int:
            stack.append(stack.pop() * group)
            return
        else:
            group = stack.pop() + group
        return self.consolidate(stack, group)