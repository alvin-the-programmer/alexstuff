class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
      memo = {}
      return self.min_steps(ring, key, memo)

    def min_steps(self, ring, key, memo, ring_idx = 0, key_idx = 0):
      key_in_memo = (ring_idx, key_idx)

      if key_in_memo in memo:
        return memo[key_in_memo]

      if key_idx == len(key):
        return 0
      
      best_attempt = float('inf')
      target = key[key_idx]

      for candidate_idx in range(0, len(ring)):
        turn_steps_without_wrap = abs(candidate_idx - ring_idx)        
        turn_steps_with_wrap = len(ring) - turn_steps_without_wrap
        turn_steps = min(turn_steps_without_wrap, turn_steps_with_wrap)

        if ring[candidate_idx] == target:
          remaining_steps = self.min_steps(ring, key, memo, candidate_idx, key_idx + 1)
          
          attempted_steps = turn_steps + remaining_steps + 1
          best_attempt = min(best_attempt, attempted_steps)

      memo[key_in_memo] = best_attempt
      return memo[key_in_memo]

# recursion
# clockwise: 4
# anti: 3
# ring-length: 7
# ring = "01234x6" ,  ring_idx = 1
# key = "x",

# ring = "01x345678" ,  ring_idx = 7

# TODOS:
#   - ring wrap around logic
#   X counting the number of moves (inc button press)

# ring=xaybbbbbyzbb, key = xyz, idx = 2, key_idx=0


coins = [1,4, 5]
target = 8
5 , 1, 1, 1
4, 4

# button
# clockwise - 2
# button
# anti - 5
# button
# 10 total

# button
# anti-4
# button
# clockwise-1
# button
# 8


# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
# For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.

# Length of both ring and key will be in range 1 to 100.
# There are only lowercase letters in both strings and might be some duplcate characters in both strings.
# It's guaranteed that string key could always be spelled by rotating the string ring.