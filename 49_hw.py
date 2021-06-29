# https://leetcode.com/problems/knight-probability-in-chessboard/solution/
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
            
        topLeft = self.knightProbabilityHelper(N, K-1, r - 1, c - 2, memo)
        topOLeft = self.knightProbabilityHelper(N, K-1, r - 2, c - 1, memo)
        topORight = self.knightProbabilityHelper(N, K-1, r - 2, c + 1, memo)
        topRight = self.knightProbabilityHelper(N, K-1, r - 1, c + 2, memo)

        botLeft = self.knightProbabilityHelper(N, K-1, r + 1, c - 2, memo)
        botOLeft = self.knightProbabilityHelper(N, K-1, r + 2, c - 1, memo)
        botRight = self.knightProbabilityHelper(N, K-1, r + 2, c + 1, memo)
        botORight = self.knightProbabilityHelper(N, K-1, r + 1, c + 2, memo)

        memo[key] = 1/8 * (topLeft + topOLeft + topORight + topRight + botLeft + botOLeft + botRight + botORight)
        
        return memo[key]

# time complexity BEFORE memo:
# K = number of turns
# O(8^K)
# space:
# O(k) call stack

# time complexity AFTER memo:
# O(Krc)
# space:
# O(k) call stack

# https://leetcode.com/problems/out-of-boundary-paths/submissions/
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        memo = {}
        return self.findPathsHelper(m, n, N, i, j, memo)
        
    def findPathsHelper(self, m, n, N, i, j, memo):
        key = (N, i, j)
        
        if key in memo:
            return memo[key]
        
        if i < 0 or i > m - 1 or j < 0 or j > n - 1:
            return 1
        
        if N <= 0:
            return 0
    
        top = self.findPathsHelper(m, n, N - 1, i - 1, j, memo)
        bottom = self.findPathsHelper(m, n, N - 1, i + 1, j, memo)
        left = self.findPathsHelper(m, n, N - 1, i, j - 1, memo)
        right = self.findPathsHelper(m, n, N - 1, i, j + 1, memo)
        
        memo[key] = (top + bottom + left + right) % (((10)**9) + 7)
        
        return memo[key]

# time complexity before memo:
# O(4^N)
# space:
# O(N) for call stack

# after memo:
# O(Nij)
# space:
# O(N) for call stack

# https://leetcode.com/problems/unique-paths-iii/submissions/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        zeroCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start = (row, col)
                if grid[row][col] == 0:
                    zeroCount += 1
        return self.uniquePathsIIIHelper(zeroCount, grid, start[0], start[1])
        
    def uniquePathsIIIHelper(self, zeroCount, grid, r, c):
        if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1:
            return 0
        
        if grid[r][c] == 2 and zeroCount == 0:
            return 1
        
        if grid[r][c] == 2:
            return 0
        
        if grid[r][c] == -1:
            return 0
        
        if grid[r][c] == 0:
            zeroCount -= 1
        
        curr = grid[r][c]
        
        grid[r][c] = -1
        
        top = self.uniquePathsIIIHelper(zeroCount, grid, r - 1, c)
        bottom = self.uniquePathsIIIHelper(zeroCount, grid, r + 1, c)
        left = self.uniquePathsIIIHelper(zeroCount, grid, r, c - 1)
        right = self.uniquePathsIIIHelper(zeroCount, grid, r, c + 1)
        
        grid[r][c] = curr
        
        return top + bottom + left + right

# https://en.wikipedia.org/wiki/Hamiltonian_path

# time complexity:
# O(4^(rc)) or O(3^(rc))? because we can go back to a spot we've already been on, so we always only have 3 choices after the first initial move
# space:
# O(rc) for call stack? (every single space on the board needs to be hit once)


# djikstra implement heap
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.convertToGraph(n, edges, succProb)
        return self.max_path_cost(graph, start, end)
        
    def max_path_cost(self, graph, src, dst):
        unvisited = set(graph.keys()) # 1.
        distance = {node: 0 for node in unvisited} # 2.
        
        distance[src] = 1
        
        arr = []
        for node in distance:
            tup = (-distance[node], node)
            arr.append(tup)
        print(arr)
        
        heapq.heapify(arr)

        print(arr)
        
        curr = src
        while arr:
        curr = arr.heappop()

            for neighbor in graph[curr]: # 3.
                if neighbor in unvisited:
                    neighbor_attempt = distance[curr] * graph[curr][neighbor]
                    distance[neighbor] = max(distance[neighbor], neighbor_attempt)
                    
            unvisited.remove(curr) # 4.
            curr = None
            
           
            # for next_node in unvisited: # 6.
            #     if curr is None or distance[next_node] > distance[curr]:
            #         curr = next_node

        return distance[dst]
    
    def convertToGraph(self, n, edges, succProb):
        graph = {}
        
        for idx in range(n):
            graph[idx] = {}
            
        for idx, edge in enumerate(edges):
            src, dest = edge
            graph[src][dest] = succProb[idx]
            graph[dest][src] = succProb[idx]
        
        return graph
