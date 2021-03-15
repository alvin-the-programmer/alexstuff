def binary_to_decimal(binStr):
    powers = len(binStr)
    binarySum = 0
    for idx, num in enumerate(binStr):
        if num == '1':
            binarySum += 2 ** (powers - idx - 1)
    return binarySum


print(binary_to_decimal("1101"))  # 13


def powers_of_2(decInt):
    start = 0
    currNum = 0
    output = []
    while 2 ** start <= decInt:
        currNum = 2 ** start
        output.append(currNum)
        start += 1
    return output


# decimal_to_binary(13)  # 1101

# print(powers_of_2(13))

def decimal_to_binary_ones_counter(decInt):
    numsToChoose = powers_of_2(decInt)

    copyOfDecInt = decInt
    counter = 0
    # binaryStr = ""
    for num in numsToChoose[::-1]:
        if num <= copyOfDecInt:
            copyOfDecInt -= num
            counter += 1
    return counter


# print(decimal_to_binary(13))  # 1101


def countBits(num):
    output = []
    for i in range(num + 1):
        output.append(decimal_to_binary_ones_counter(i))
    return output


print(countBits(2))

# num = 8
# [0,1,1,2,1,2,2,3,1,2]

print(decimal_to_binary_ones_counter(9))

# recursive tree idea
