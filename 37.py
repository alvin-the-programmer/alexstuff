def subsets_of_size(items, size):
  if size == 0:
    return [[]]
  output = []
  for idx, item in enumerate(items):
    subsets = subsets_of_size(items[idx+1:], size - 1)
    for subset in subsets:
      output.append([item] + subset)

  return output

# print(subsets_of_size([7, 1, 8], 2))
print(subsets_of_size([7, 1, 8, 4], 3))
