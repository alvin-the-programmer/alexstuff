# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.


# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:

# Input: words = ["z","x"]
# Output: "zx"
# Example 3:

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.


const removeBoxes = (boxes,) = > {
  if (boxes.length === 0)
    return 0;

  let lo = 0;
  let hi = 0;
  let max = -Infinity;
  while (hi <= boxes.length) {
    if (boxes[lo] === boxes[hi]) {
      hi += 1;} else {
      const attempt = (hi - lo) ** 2 + removeBoxes([...boxes.slice(0, lo), ...boxes.slice(hi)])
      max = Math.max(attempt, max);
      lo = hi;}
  }
  return max;
