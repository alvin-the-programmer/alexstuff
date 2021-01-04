# whiteboard: https://awwapp.com/b/urw2wglksctdz/

# def factorial(n):
#   if n == 1:
#     return 1
#   return n * factorial(n - 1)

# Write function called `fact` that takes in a number n, and returns the factorial of n
#
# factorial(4) # 4 * (3 * 2 * 1) = 24
# factorial(3) # (3 * 2 * 1) = 6

# print(factorial(4))


# n = length of list
# time: O(n)
# def sum_list(li):
#     if len(li) == 0:
#         return 0
#     return li.pop() + sum_list(li)

# # n = length of list
# # time: O(n^2)
# def sum_list(li):
#     if len(li) == 0:
#         return 0
#     last_el = li[-1]
#     li_without_last = li[:-1]
#     return last_el + sum_list(li_without_last)

# Write a function that takes in a list of numbers and returns their sum
# solve this recursively.

# my_list = [3, 1, 7]
# print(sum_list(my_list)) # 11
# print(my_list)


# time: O(n)
# def foo(n):
#   for i in range(0, n):
#     print(i)

# time: O(n-c) -> O(n)
# def foo(n):
#   for i in range(0, n - 9999999999999):
#     print(i)


# time: O(n / 2) -> O(n)
# def foo(n):
#   for i in range(0, int(n)):
#     print(i)

# foo(50)

# time: O(n + n) -> O(2n) -> O(n)
# def foo(n):
#   for i in range(0, int(n)):
#     print(i)

#   for i in range(0, int(n)):
#     print(i)

# time: O(n)
# def foo(n):
#   if n == 0:
#     return
#   foo(n - 1)


# 10 -> 9 -> 8 -> ... 0


# time: O(n/2) -> O(n)
# def foo(n):
#   if n == 0:
#     return
#   foo(n - 2)


# time: O(2^n)
# def foo(n):
#   if n == 0:
#     return
#   foo(n - 1)
#   foo(n - 1)

# time: O(3^n)
# def foo(n):
#   if n == 0:
#     return
#   foo(n - 1)
#   foo(n - 1)
#   foo(n - 1)


# import time

# def sum_list_fast(li):
#     if len(li) == 0:
#         return 0
#     return li.pop() + sum_list_fast(li)

# def sum_list_slow(li):
#     if len(li) == 0:
#         return 0
#     last_el = li[-1]
#     li_without_last = li[:-1]
#     return last_el + sum_list_slow(li_without_last)


# array = []
# for i in range(0, 800):
#   array.append(5)

# start = time.time()
# sum_list_fast(array)
# end = time.time()
# print((end - start))


# array = []
# for i in range(0, 800):
#   array.append(5)

# start = time.time()
# sum_list_slow(array)
# end = time.time()
# print((end - start))


# O(1) - constant
# O(n) - linear
# O(n^c) - polynomial
  # O(n^2) - quadratic
  # O(n^3) - cubic
# O(c^n) - exponential
  # O(2^n) 
  # O(2^n) 
