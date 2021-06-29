sentence = "follow the yellow brick road"
synonyms = {
  "follow": ["chase", "pursue"],
  "yellow": ["gold", "amber", "lemon"],
}

substitute_synonyms(sentence, synonyms)
# [
#   'chase the gold brick road',
#   'chase the amber brick road',
#   'chase the lemon brick road',
#   'pursue the gold brick road',
#   'pursue the amber brick road',
#   'pursue the lemon brick road'
# ]


# ['']
# 
        #         follow the yellow brick road = 
        #    chase /  \ pursue
        # the yellow brick road
        #          \ ['lemon brick road', 'amber brick road', 'gold brick road']
        #          yellow brick road = ['lemon brick road', 'amber brick road', 'gold brick road']
        #            /lemon   \amber   \gold
        #            brick road = ['brick road']
        #              \
        #              road = ['road']
        #               \
        #               ''  => ['']

# n = # of words in sentence
# s = max # of synonyms for ONE word
# time = O(ns)
# branching factor = s
# height = n
# O(s^n)

from collections import deque
def substitute_synonyms(sentence, synonyms):
    words = sentence.split(' ')             #['hello']
    words = deque(words)
    return substitute_synonyms_helper(words, synonyms, 0)  # ['hello ']

def substitute_synonyms_helper(words, synonyms, idx):
    if idx == len(words):
        return ['']

    first_word = words[idx]

    if first_word in synonyms:
        replacements = synonyms[first_word]
        output = []
        for replacement in replacements:
            suffixes = substitute_synonyms_helper(words, synonyms, idx + 1) # ['']
            for suffix in suffixes:
                if suffix != '':
                    output.append(replacement + ' ' + suffix)
                else:
                    output.append(replacement)
        return output
    else:
        output = []
        suffixes = substitute_synonyms_helper(words, synonyms, idx + 1) #['']
        for suffix in suffixes:
            if suffix != '':
                output.append(first_word + ' ' + suffix)
            else:
                output.append(first_word)
        return output
        
# https://staging.structy.net/problems/premium/substitute-synonyms

# sentence = 'hello'
# synonyms = {}

https://leetcode.com/explore/interview/card/amazon/84/recursion/521/


https://leetcode.com/problems/kth-largest-element-in-an-array/