class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        memo = {}
        return self.knightProbabilityHelper(N, K, r, c, memo)
    
    def knightProbabilityHelper(self, N, K, r, c, memo):
        key = (K, r, c)
        
        if key in memo:
            return memo[key]
        
        if r >= 0 and r <= N - 1 and c >= 0 and c <= N - 1:
            if K == 0:
                return 1
        else:
            return 0
            
        topLeft = self.knightProbabilityHelper(N, K-1, r - 1, c - 2, memo) / 8
        topOLeft = self.knightProbabilityHelper(N, K-1, r - 2, c - 1, memo) / 8
        topORight = self.knightProbabilityHelper(N, K-1, r - 2, c + 1, memo) / 8
        topRight = self.knightProbabilityHelper(N, K-1, r - 1, c + 2, memo) / 8

        botLeft = self.knightProbabilityHelper(N, K-1, r + 1, c - 2, memo) / 8
        botOLeft = self.knightProbabilityHelper(N, K-1, r + 2, c - 1, memo) / 8
        botRight = self.knightProbabilityHelper(N, K-1, r + 2, c + 1, memo) / 8
        botORight = self.knightProbabilityHelper(N, K-1, r + 1, c + 2, memo) / 8

        memo[key] = (topLeft + topOLeft + topORight + topRight + botLeft + botOLeft + botRight + botORight)
        
        return memo[key]

# https://leetcode.com/problems/knight-probability-in-chessboard/





class Solution:
  def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
    row_inbounds = 0 <= r < N
    col_inbounds = 0 <= c < N
    
    inbounds = row_inbounds and col_inbounds
    
    if K == 0:
      if inbounds:
      	return 1
      else:
      	return 0
    elif not inbounds:
    	return 0

    total_probability = 0
    for neighbor in self.neighbors(r, c):
      neighbor_r, neighbor_c = neighbor
      total_probability += (1/8) * self.knightProbability(N, K - 1, neighbor_r, neighbor_c)

    return total_probability

  def neighbors(self, r, c):
    deltas = [
      ( -1, -2),
      ( -1,  2),
      (  1, -2),
      (  1,  2),
      ( -2, -1),
      (  2, -1),
      ( -2,  1),
      (  2,  1)
    ]

    return [ (r + delta[0], c + delta[1]) for delta in deltas ]
