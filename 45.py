def mergeSort(arr):
    if len(arr) == 1:
        return arr

    middleIdx = len(arr) // 2

    left = mergeSort(arr[:middleIdx]) # n
    right = mergeSort(arr[middleIdx:]) # n

    leftPtr = 0
    rightPtr = 0

    newArr = []

    while leftPtr < len(left) and rightPtr < len(right): # n
        if left[leftPtr] <= right[rightPtr]:
            newArr.append(left[leftPtr]) 
            leftPtr += 1
        else:
            newArr.append(right[rightPtr])
            rightPtr += 1

    newArr += left[leftPtr:] + right[rightPtr:] # n

    return newArr
    

# inp = [10, 4, 5, 6, 7, 10, 20, 100, 101]

import random
# print(random.randint(0, 10)) # random bw 0 -10
# print(random.randrange(0, 10)) # bw 0 -9
inp = [ random.randint(0, 100) for i in range(0, 20000) ]

print(mergeSort(inp))
