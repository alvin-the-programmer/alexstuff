class Node:
    def __init__(self):
        self.edges = {}
        self.terminal = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        self._insert(self.root, s)

    def _insert(self, node, s, idx = 0):
        if idx >= len(s):
          node.terminal = True
          return
        
        first = s[idx]
        if first not in node.edges:
            node.edges[first] = Node()

        self._insert(node.edges[first], s, idx + 1)
    
    def search(self, s):
        return self._search(self.root, s)

    def _search(self, node, s, idx = 0):
        if idx >= len(s):
          return node.terminal
        
        first = s[idx]
        if first in node.edges:
          return self._search(node.edges[first], s, idx + 1)
        else:
          return False

    def startsWith(self, prefix):
      return self._startsWith(self.root, prefix)

    def _startsWith(self, node, s, idx = 0):
      if idx >= len(s):
        return True
      
      first = s[idx]
      if first in node.edges:
        return self._startsWith(node.edges[first], s, idx + 1)
      else:
        return False
    

# s = len str
# n = # words

# words heavily share prefixes

# Trie:
#   - stores strings for lookup O(s)
#   - saves space for shared prefixed chars

# Set:
#   - store strings for lookup O(s)
#   - must use space for every char

# apple
#  pp
#   8 units



trie = Trie()

trie.insert('cat')
trie.insert('cap')
trie.insert('caterpillar')
trie.insert('dog')
trie.insert('doggo')
trie.insert('door')
trie.insert('hidden')
trie.insert('hideout')

print(trie.has('cat')) # True
print(trie.has('cap')) # True
print(trie.has('caterpillar')) # True
print(trie.has('dog')) # True
print(trie.has('doggo')) # True
print(trie.has('door')) # True
print(trie.has('hidden')) # True
print(trie.has('hideout')) # True

print(trie.has('do')) # False
print(trie.has('donut')) # False
print(trie.has('zoo')) # False
print(trie.has('cater')) # False
print(trie.has('dogged')) # False



# https://leetcode.com/problems/implement-trie-prefix-tree/







https://leetcode.com/problems/max-area-of-island/

