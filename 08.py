# def sum_array(array):
#   if len(array) == 0:
#     return 0
#   else:
#     return array[0] + sum_array(array[1:])

# print(sum_array([3,2, 4])) # 9
  
  
def sum_array(array, res = 0):
    if len(array) == 0:
    	return res
    else:
    	return sum_array(array[1:], array[0] + res)

print(sum_array([3,2, 4])) # 9
