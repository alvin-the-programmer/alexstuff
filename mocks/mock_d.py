# https://awwapp.com/b/uyjwo06tsoozm/

# Write a fn that takes in a amount (amt) of money and a list of coin values (coins).
# Return the min number of coints that can provide change for the given amount

def best_change(total, coins):
    memo = {}
    return best_change_helper(total, coins, memo)

def best_change_helper(total, coins, memo):
    key = total

    if key in memo:
        return memo[key]

    if total == 0:
        return 0
    if total < 0:
        return float("inf")

    minimum = float("inf")

    for coin in coins:
        num_of_coins = 1 + best_change_helper(total - coin, coins, memo)
        if num_of_coins < minimum:
            minimum = num_of_coins

    memo[key] = minimum
    return memo[key]

print(best_change(8, [ 5, 1, 4 ])) # 2
print(best_change(100, [ 1, 10, 15, 25 ])) # 4
