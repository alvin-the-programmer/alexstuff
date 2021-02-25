# Problem:

# input1: [(a, b, equal), (b, a, not-equal)]
# Output2: false

# Input2: [
#  (a, b, equal), 
#  (b, c, equal),
#  (a, c, equal)
# ]
# Output2: true



# Input2: [
#  (a, b, equal), 
#  (b, c, equal),
#  (a, c, not-equal)
# ]
# Output2: false


# __________________________
	

# sqrt(n) = # of nodes
# n = edges

def validate_equations(edges):
	components = {}
	for edge in edges:
		nodeA, nodeB, _ = edge
		dict[nodeA] = nodeA
		dict[nodeB] = nodeB

	for edge in edges: # O(n^2)
		nodeA, nodeB, eq = edge
		if eq == 'equal':
			union(dict, nodeA, nodeB) # O(n)

	for edge in edges: #O(n^2)
		nodeA, nodeB, bool = edge
		if bool == 'not-equal':
			if find(dict, nodeA) == find(dict, nodeB): #O(n)
				return False
	return True

def find(dict, teammate):
	if dict[teammate] == teammate:
		return teammate
	return find(dict, dict[teammate])

def union(dict, nodeA, nodeB):
	parent_nodeA = find(dict, nodeA)
	parent_nodeB = find(dict, nodeB)

	dict[parent_nodeA] = parent_nodeB

time: O(n^1.5)
space: O(sqrt(n))

https://leetcode.com/problems/satisfiability-of-equality-equations/

