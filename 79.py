# https://leetcode.com/problems/concatenated-words/


# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

# O(n^2w^2)
# n

from typing import List

# w * (w + ttw)
# ttww
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        concatenated = []
        
        for idx, word in enumerate(words): #
            bank = words[:idx] + words[idx+1:]
            if word != '' and  self.concat_poss(word, bank) == True: 
                concatenated.append(word)
        return concatenated

    # O(ttw)
    def concat_poss(self, target, words):
        table = [False] * (len(target) + 1)
        table[0] = True

        for i in range(len(table)):
            if table[i] == True:
                for word in words:
                    if target[i:].startswith(word):
                        table[i + len(word)] = True
        return table[-1]

    # def concat_poss(self, target, words, memo):
    #     if target in memo:
    #         return memo[target]
    #     if not words:
    #         return False

    #     if not target:
    #         return True

    #     for word in words: # O(n)
    #         if target.startswith(word):
    #             if self.concat_poss(target[len(word):], words, memo):
    #                 memo[target] = True
    #                 return True

    #     memo[target] = False
    #     return memo[target]

# s = Solution()

# print(s.concat_poss('catsanddog', ['cats', 'sand', 'dog']))

# print(s.findAllConcatenatedWordsInADict(['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaa',  ]))
# import sys
# print(sys.getrecursionlimit())


#O(n * (n + (n^t) ))
#O(n^2 + n((n^t))
#O(n((n^t))

# 'aaaa', ['a', 'aa', 'aaa']


#            aaaa
#  a    /      | aa        \ aaa  
#     aaa         [aa]          a
# a/ aa| aaa\
# [aa]


#         ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
        
#         ["A", "B", "BDB", "D"]      [ABABAB]
#            A /   /   \      \
# [A, B, BDB, D]   
#         "A"     "B"  "BDB"  "D" 


#         concat_poss("BDB", ["A", "B", "D"])

# what was a challenge?
"""
normalizing tables
    structure tables
    PROs for normalization
        3rd normal form for schema - https://en.wikipedia.org/wiki/Third_normal_form
            - Avoids column duplication
            - notebooks <-> notes <-> tags
            - must update duplicated columns
            - can lead to being out of sync
            - if duplicates, what is the source of truth
        use join table to avoid column duplication
            - person table can reference both applicants and students
        doing complex queries is easy
    CONs
      - having joins is very slow

    putting JSON as a column of a table
"""

   persons
# id Name     Age                 Test           
   0 "alvin"     27         "{test1:100, test2:300}"
   1 "alvin"     22         "{test1:100, test2:300}"
   2 "alvin"     28         "{test1:100, test2:300}"
   3 "alvin"     28         "{test1:100, test2:300}"


# select * from persons where Test include "test:100"


# https://en.wikipedia.org/wiki/B-tree