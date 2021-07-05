# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digit_logs = []
#         letter_logs = []

#         for log in logs:
#             start = log.find(' ')
#             new_log = ''.join(log[start + 1:].split(' '))
#             if new_log.isalpha():
#                 letter_logs.append(log)
#             else:
#                 digit_logs.append(log)
        
#         letter_dict = {}
#         for log in letter_logs:
#             words = log.split(' ')
#             letter_dict[words[0]] = ' '.join(words[1:])

#         print(letter_dict)

#         letter_logs.sort(key = lambda log: ( letter_dict[log[:log.find(' ')]], log[:log.find(' ')] ))
#         letter_logs += digit_logs

#         return letter_logs


# n = # of logs
# x = max length of each log
# time = O(nx + nlogn)
# space = O(nx or n)

# O(xnlogn)   vs    O(n*x + n*logn)
#  O(n * (xlogn))       O(n(x + logn))


a*b

a+b
class Solution:
    def reorderLogFiles(self, logs):
        digit_logs = []
        letter_logs = []
        for log in logs:
            segments = log.split(' ')
            identifier = segments[0]
            content = ''.join(segments[1:])
            if content.isalpha():
                letter_logs.append((identifier, ' '.join(segments[1:])))
            else:
                digit_logs.append(log)

        print(letter_logs)

        letter_logs.sort(key=lambda item: (item[1], item[0]))
        
        sorted_letter_logs = [ ' '.join(letter_log) for letter_log in letter_logs]
        return sorted_letter_logs + digit_logs

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

s = Solution()
s.reorderLogFiles(logs)