""" 
Input:
    path: '%USER%->%ROLE%/%ROOT%/desktop/%DATE%',
    tokens: {
        'USER': 'azablan',
        'DATE': '06-15-2021',
        'ROLE': 'dev',
        'ROOT': 'main/tmp'
    }

Output: 'azablan->dev/main/tmp/desktop/06-15-2021.txt'
"""

# PART 1
def replace_tokens(path, tokens):
    position = 0
    new_paths = []
    while position < len(path):
        curr = path[position]

        if curr == '%':
            closer_idx = path.index('%', position + 1)
            new_paths.append(tokens[path[position + 1: closer_idx]])
            position = closer_idx
        else:
            new_paths.append(curr)
        
        position += 1

    return ''.join(new_paths)

# path = '%USER%->%ROLE%/%ROOT%/desktop/%DATE%'
# tokens = {
#     'USER': 'azablan',
#     'DATE': '06-15-2021',
#     'ROLE': 'dev',
#     'ROOT': 'main/tmp'
# }

# print(replace_tokens(path, tokens))

path = '%USER%/%ROOT%/desktop/%DATE%/%A%/%B%/%C%.txt'
tokens = {
    'USER': 'azablan->%ROLE%',
    'DATE': '06-15-2021',
    'ROLE': 'dev',
    'ROOT': 'main/tmp',
    'A': 'one%B%%C%',
    'B': 'two',
    'C': 'three%D%',
    'D': 'LOL'
}

# PART 2
def evaluate_tokens(tokens):
    evaluated = {}
    for key in tokens:
        evaluated_token = df_eval(tokens, key)
        evaluated[key] = evaluated_token
    return evaluated

def df_eval(tokens, key):
    value = tokens[key]
    position = 0
    new_paths = []
    while position < len(value):
        curr = value[position]

        if curr == '%':
            closer_idx = value.index('%', position + 1)
            neighbor = value[position + 1: closer_idx]
            neighbor_eval = df_eval(tokens, neighbor)
            new_paths.append(neighbor_eval)
            position = closer_idx
        else:
            new_paths.append(curr)
        
        position += 1

    answer = ''.join(new_paths)
    tokens[key] = answer
    return answer
    
def replace_tokens_2(path, tokens):
    evaluated_tokens = evaluate_tokens(tokens)
    return replace_tokens(path, evaluated_tokens)

print(replace_tokens_2(path, tokens))

# print(evaluate_tokens(tokens))
# print(df_eval(tokens, 'C'))