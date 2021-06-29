# %USER%/main/%ROOT%/%DATE%

# USER="azab"
# ROOT="desktop/projects/google"
# DATE="06-14-2021"
# position="dev"



# {"user": "azab", }


# replace_tokens('%USER%-%POSITION%/main/%ROOT%/%DATE%', {"USER": "azab", ... })
# -> azab-dev/main/desktop/projects/google/06-13-2021
# 
# -%POSITION%/main/%ROOT%/%DATE%/readme.txt
#      i                
# 
# ["azab", "-", "dev", "/", "m", "desktop/projects/google", "/", "06-14-2021"]
# return joim(arr)
# 
# n = len(format)
# v = longest value in tokens

# Time: (n * v)

# '%x%%x%%x%...'
# {x: 'aaaaaaaaaaaaaaaa...',  }

# aaaaaaaaaaaaaaa...

def replace_tokens(format, tokens):
    i = 0
    result = []

    while i < len(format):
        curr = format[i]
        if curr == "%":
            i += 1
            closer = format.index("%", i)
            # if "%" in tokens[format[i:closer]]:
            
            result.append(tokens[format[i:closer]])
            i = closer + 1
        else:
            result.append(format[i])
            i += 1
    
    return "".join(result)

# out = replace_tokens('%USER%=>%POSITION%/main/%ROOT%/%DATE%/readme.txt', {
#   "USER": "azab",
#   "POSITION": "dev",
#   "ROOT": "desktop/projects/google",
#   "DATE": "06-14-2021"
# })

# print(out)

replace_tokens('%USER%=>%POSITION%/main/%ROOT%/%DATE%/readme.txt', {
  "USER": "azab",
  "POSITION": "dev",
  "ROOT": "/%LOCATION%/%DESKTOP%/projects/google",
  "DATE": "06-14-2021",
  "LOCATION": "%DATE%/NYC",
  "A": "stuff"
})

{
    "a": '%b%%c%',
    "d": "%b%",
    "b": "one%x%",
    "x": "two%y%",
    "y": "three%z%"
    "z": "stoppp"
}

dp: { "b": "onetwothreestoppp" }

# b = max # of tokens in one value
# n = # of keys in tokens object
# b^n

# for every k,v in tokens
#   recursively(dfs) evaluate each value using the same tokens
#    "replace_tokens(v, tokens)
# replace_tokens(orig_str,new_tokens)