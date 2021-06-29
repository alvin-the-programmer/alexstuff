# Dynamic Programming
#    -recursive memoization
#    -iterative tabulation


# def coin_change(coins, amt):
#     table = [False] * (amt + 1)
#     table[0] = True
#     for i in range(len(table)):
#         if table[i] == True:
#             for coin in coins:
#                 next_amt = i + coin
#                 if next_amt < len(table):
#                     table[next_amt] = True

#     return table[amt]


# print(coin_change([2, 5], 6))  # True
# print(coin_change([2, 5], 3))  # False
# print(coin_change([3, 11, 5], 8))  # True
# print(coin_change([3, 11, 5], 12))  # True
# print(coin_change([3, 11, 5], 7))  # False


# best_change([1, 4, 5], 8) # = 2
# best_change([7, 3], 6)

# [1, 4, 5]
# # min num of coins
# [0 1 2 3 1 1 2 3 2]
#  0 1 2 3 4 5 6 7 8


def best_change(coins, amt):
    table = [None] * (amt + 1)
    table[0] = 0

    for i in range(len(table)):
        if table[i] != None:
            for coin in coins:
                next_amt = i + coin
                if next_amt < len(table):
                    if table[next_amt] == None or table[next_amt] > table[i] + 1:
                        table[next_amt] = table[i] + 1

    return table[amt]


print(best_change([1, 4, 5], 8))  # 2
print(best_change([7, 3], 5))  # none
