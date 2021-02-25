# // The tribonacci sequence is a seq of integers
# //      n:  0 1 2 3 4 5 6  7   8
# // trib(n): 0 1 1 2 4 7 13 24 44

# // trib(8); // 44

# trib(8) = trib(7) + trib(6) + trib(5)

def trib(n):
    memo = {}
    return tribHelper(n, memo)

def tribHelper(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    memo[n] = tribHelper(n - 1, memo) + tribHelper(n - 2, memo) + tribHelper(n - 3, memo)
    return memo[n]

print(trib(7)) # 24
print(trib(8)) # 44
print(trib(40)) # 44


# https://oeis.org/