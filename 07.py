
# https://awwapp.com/b/uxbjhjacaqfqo/

def decodeString(self, s: str) -> str:
    numbers = []
    letters = []
    i = 0
    result = ""
    
    while i < len(s):
        if s[i].isdigit():
            num = s[i]
            if s[i+1].isdigit():
                num += s[i+1]
                i += 1
                if s[i+2].isdigit():
                    num += s[i+2]
                    i += 1
            numbers.append(num)
        
        word = ""
        
#           when we hit a closing bracket, pop the letters array?
        while s[i].isalpha() and s[i] != '[' and s[i] != ']':
            word += s[i]
            i += 1
        letters.append(word)
        i += 1