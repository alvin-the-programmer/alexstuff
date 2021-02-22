class Solution:
    def countComponents(self, n, edges):
        components = []
        for idx in range(n):
            components.append(idx)

        print(components)
        def find(a):
          if a == components[a]:
            return a
          return find(components[a])

        def union(a, b):
          if find(a) != find(b):
            components[a] = find(b)
        
        for edge in edges:
          a, b = edge
          union(a, b)

        counter = 0

        print(components)
        for idx, captain in enumerate(components):
            if idx == captain:
                counter+=1
        
        return counter


s = Solution()
print(s.countComponents(5, [[0,1],[0,2],[2,3],[2,4]]))


# [[0,1],[0,2],[2,3],[2,4]]