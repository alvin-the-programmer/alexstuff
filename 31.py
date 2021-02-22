# master set: [x, y, z]
# 
# x
# y
# z
# xy
# xz
# yz
# xyz

def subsets(items):
  if not items:
    return [[]]
  first_item, *rest_items = items
  subs_without_first = subsets(rest_items)
  subs_with_first = []
  for sub in subs_without_first:
    duplicated_sub = [*sub, first_item]
    subs_with_first.append(duplicated_sub)

  return subs_with_first + subs_without_first

# print(subsets(['x', 'y', 'z']))

# subs([x, y, z])
#     -> subs([y, z])
#         [
#           [],
#           [y],
#           [z],
#           [y, z],
#         ]


# https://awwapp.com/b/uiqu13k0ttvhu/

def permutations(items):
    if not items:
        return [[]]
    
    first_item, *rest_items = items
    subs_without_first = permutations(rest_items)
    subs_with_first = []
    for sub in subs_without_first:
        for idx in range(len(sub) + 1):
            dupe = [ *sub ]
            dupe.insert(idx, first_item)
            subs_with_first.append(dupe)
    return subs_with_first

print(permutations(['x', 'y', 'z']))
    
# permutations([x,y,z])
#   -> permutations([y,z])
        # [
        #   [y, z]
        #   [z, y]
        # ]

# https://leetcode.com/problems/permutations/