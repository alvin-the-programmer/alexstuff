# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
        



# Write a function, tolerant_teams, that takes in a list of rivalries as an argument. 
# A rivalry is a pair of people who should not be placed on the same team. 
# The function should return a boolean indicating whether or not it is possible to separate 
# people into two teams, without rivals being on the same team. 
# The two teams formed do not have to be the same size.

# tolerant_teams([
#   ('philip', 'seb'),
#   ('raj', 'nader')
# ]) # -> True
# graph = {
# philip: [seb],
# seb: [philip],
# raj: [nader],
# nader: [raj]
# }

"""
blue (set)
philip
raj

red (set)
seb
nader
"""

# tolerant_teams([
#   ('philip', 'seb'),
#   ('raj', 'nader'),
#   ('raj', 'philip'),
#   ('seb', 'raj')
# ]) # -> False

from collections import defaultdict
# True = Blue
# False = Red
def tolerant_teams(rivalries):
    graph = create_graph(rivalries)
    teams = {}

    for person in graph:
        if person not in teams:
            if dfs_traverse(person, graph, teams, True) == False:
                return False
                
    return True

def dfs_traverse(person, graph, teams, color):
    if person in teams:
        return teams[person] == color
    
    teams[person] = color
    neighbors = graph[person]

    for neighbor in neighbors:
        if dfs_traverse(neighbor, graph, teams, not color) == False:
            return False

    return True

def create_graph(rivalries):
    graph = defaultdict(set)

    for person_a, person_b in rivalries:
        graph[person_a].add(person_b)
        graph[person_b].add(person_a)

    return graph

print(tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader')
])) # -> True

print(tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader'),
  ('raj', 'philip'),
  ('seb', 'raj')
])) # -> False

# https://staging.structy.net/purchase

# 4242 4242 4242 4242

# https://staging.structy.net/problems/premium/tolerant-teams

def is_graph_bipartite(players, rivalries):
    graph = create_graph(players, rivalries)
    teams = {}

    for person in graph:
        if person not in teams:
            if df_traverse(person, graph, teams, True) == False:
                print("The force is not strong")
                return False
    
    print("The force is strong.")
    return True

def df_traverse(person, graph, teams, color):
    if person in teams:
        return teams[person] == color
    
    teams[person] = color
    neighbors = graph[person]

    for neighbor in neighbors:
        if df_traverse(neighbor, graph, teams, not color) == False:
            return False

    return True

def create_graph(players, rivalries):
    graph = {}

    for player in players:
        graph[player] = set()

    for player_1, player_2 in rivalries:
        graph[player_1].add(player_2)
        graph[player_2].add(player_1)

    return graph

characters_1 = ('darth', 'luke', 'kylo')
graph_1 = [('darth', 'luke'), ('luke', 'kylo')] # The force is strong

characters_2 = ('padme', 'din', 'silman', 'kylo')
graph_2 = [('padme', 'din'), ('din', 'silman'), ('silman', 'padme')] # The force is not strong

is_graph_bipartite(characters_1, graph_1)
is_graph_bipartite(characters_2, graph_2)