class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_graph = self.convertToGraph(n, red_edges)
        blue_graph = self.convertToGraph(n, blue_edges)
        
        output = []
        
        for i in range(n):
            blueVisited = set()
            redVisited = set()
            blueMemo = {}
            redMemo = {}
            
            blueStart = self.traverseGraph(0, i, red_graph, blue_graph, 'blue', blueVisited, blueMemo)
            redStart = self.traverseGraph(0, i, red_graph, blue_graph, 'red', redVisited, redMemo)
         
            if blueStart >= 0 and redStart >= 0:
                final = blueStart if blueStart < redStart else redStart
                output.append(final)
            elif blueStart < 0 and redStart < 0:
                output.append(blueStart)
            else:
                final = blueStart if blueStart > redStart else redStart
                output.append(final)
                
        return output
        
    def convertToGraph(self, n, edges):
        graph = {}
        
        for idx in range(n):
            graph[idx] = []
        
        for edge in edges:
            [source, dest] = edge
            graph[source].append(dest)
        
        return graph
    
    def traverseGraph(self, curr_node, dest_node, red_graph, blue_graph, curr_graph, visited, memo):
        key = (curr_node, dest_node, curr_graph)
        
        if key in memo:
            return memo[key]
        
        if curr_node == dest_node:
            return 0
        
        if (curr_node, curr_graph) in visited:
            return -1
        
        visited.add((curr_node, curr_graph))
        
        next_graph = 'red' if curr_graph == 'blue' else 'blue'
        neighbors = blue_graph[curr_node] if curr_graph == 'blue' else red_graph[curr_node]
        
        minValue = -1

        for neighbor in neighbors:
            newVisited = set(visited)
            output = self.traverseGraph(neighbor, dest_node, red_graph, blue_graph, next_graph, newVisited, memo)
            if output >= 0:
                output += 1
                if minValue == -1:
                    minValue = output
                else:
                    minValue = output if output < minValue else minValue
                    
        memo[key] = minValue
        return memo[key]

# https://awwapp.com/b/ubxwv7rbcs4bz/


# O(n + r + b)
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_graph = self.convertToGraph(n, red_edges)
        blue_graph = self.convertToGraph(n, blue_edges)

        output = [-1] * n
        output[0] = 0
        layer = [(0, None)]
        distance = 0
        visited = set((0, None))

        while layer:
            distance += 1

            new_layer = []
            for nodeTuple in layer:
                node, color = nodeTuple

                if color != 'blue':
                    for neighbor in blue_graph[node]:   
                        if (neighbor, 'blue') not in visited:
                            visited.add((neighbor, 'blue'))                     
                            new_layer.append((neighbor, 'blue'))
                if color != "red":
                    for neighbor in red_graph[node]:
                        if (neighbor, 'red') not in visited:  
                            visited.add((neighbor, 'red'))     
                            new_layer.append((neighbor, 'red'))
            # set the output distance of that nodes in the layer 
            for nodeTuple in new_layer:
                node, color = nodeTuple
                # only replace if -1
                if output[node] == -1:
                    output[node] = distance

            layer = new_layer

        return output


    def convertToGraph(self, n, edges):
        graph = {}
        
        for idx in range(n):
            graph[idx] = []
        
        for edge in edges:
            [source, dest] = edge
            graph[source].append(dest)
        
        return graph