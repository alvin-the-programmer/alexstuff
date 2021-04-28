def deepest_strings(s):
  curr_level, max_level = -1, -1
  stack = []
  openers = "([{"
  closers = ")]}"

  for idx in range(len(s)):
    curr_letter = s[idx]
    if idx == 0:
      curr_level += 1
      stack.append(curr_level)

    if curr_letter in openers:
      curr_level += 1
      stack.append(curr_level)
    elif curr_letter in closers:
      curr_level -= 1
      stack.append(curr_level)
    else:
      stack.append(curr_letter)
    
    if curr_level > max_level:
      max_level = curr_level
      
  output = []
  start_indices = [ i for i in range(len(stack)) if stack[i] == max_level ]
  for start_index in start_indices:
    end_index = stack.index(max_level - 1, start_index)
    output.append("".join(stack[start_index+1:end_index]))
  return output

# def deepest_strings(s):
#   curr_level, max_level = -1, -1
#   stack = []
#   openers = "([{"
#   closers = ")]}"

#   for idx in range(len(s)):
#     curr_letter = s[idx]
#     if idx == 0:
#       curr_level += 1
#       stack.append(curr_level)

#     if curr_letter in openers:
#       curr_level += 1
#       stack.append(curr_level)
#     elif curr_letter in closers:
#       curr_level -= 1
#       stack.append(curr_level)
#     else:
#       stack.append(curr_letter)
    
#     if curr_level > max_level:
#       max_level = curr_level
      
#   output = []
#   found = False
  
#   temp_word = ""
#   for letter in stack:
#     if type(letter) is int:
#       if int(letter) == max_level:
#         found = True
#         continue
#       else:
#         if temp_word:
#           output.append(temp_word)
#         temp_word = ""
#         found = False

#     if found == True:
#       temp_word += letter



  # return output


# type(letter) is int




# abc(def[ghi]jkl)mn[lm[lmk[mklk]]]o
# ['ghi']

# lvl: 0
# "abc(def[ghi]jkl)mno"
# stack: [0abc1def2ghi1jkl0mno]

# '''
# "abc(def)ghi" => ["def"]
# "abc(def[ghi]jkl)mno" => ["ghi"]
# "abc(def)ghi[jkl]mno" => ["def", "jkl"]
# "abc" => []
# "" => []
# (),[],{}
# '''


def deepest_strings(s):
  curr_level, max_level = 0, 0
  stack = [0]
  openers = "({["
  closers = ")]}"

  for letter in s:
    if letter in openers:
      curr_level += 1
      if curr_level > max_level:
        max_level = curr_level
      stack.append(curr_level)
    elif letter in closers:
      curr_level -= 1
      stack.append(curr_level)
    else:
      stack.append(letter)

  start_indices = [idx for idx in range(len(stack)) if stack[idx] == max_level]

  words = []
  for start in start_indices:
    end_index = stack.index(max_level - 1, start)
    words.append("".join(stack[start+1:end_index]))

  return words

# 0abc1def0ghi

print(deepest_strings("abc(def)ghi"))# ["def"]
print(deepest_strings("abc(def[ghi]jkl)mno")) # ["ghi"]
print(deepest_strings("abc(def)ghi[jkl]mno")) # ["def", "jkl"]
print(deepest_strings("abc(def)ghi[jkl](((mno)))")) # ["mno"]



