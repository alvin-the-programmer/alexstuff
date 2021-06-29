#  Write a function fib(n) that takes in a positive int n, and returns the n-th number of the fibonacci
# sequence. The first two nums of the seq are 1 and 1, to gen the next number, take the sum of the last 2.

#     n  -> 1 2 3 4 5 6  7  8  
# fib(n) -> 1 1 2 3 5 8 13 21 ...


# fib(7) -> 13


def fib(n):
  return fib_helper(n, {})

# def fib_helper(n, memo):
#     if n in memo:
#         return memo[n]
#     if n == 2 or n == 1:
#         return 1
 
#     memo[n] = fib_helper(n-1, memo) + fib_helper(n-2, memo)

#     return memo[n]



# def fib(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 2 or n == 1:
#         return 1
 
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)

#     return memo[n]

# print(fib(6)) # 8
# print(fib(7)) # 13
# print(fib(8)) # 21
# print(fib(50)) # ?

# def foo(arg=[]):
#   arg.append(7)
#   print(arg)


# foo()
# foo()


