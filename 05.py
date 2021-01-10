
# O(max(n, m))
def foo(n, m):
  if n > m:
    for i in range(0, n):
      print(i)
  else:
    for i in range(0, m):
      print(i)


# foo(100, 5)
# foo(5, 100)


#    FAST/SMALL 
# O(1) - constant X
# O(log_(n)) - logarithmic
# O(n) - linear X
# O(n * log(n)) - loglinear / quasilinear / linearithmic
# O(n^c) - polynomial
#   O(n^2) - quadratic
#   O(n^3) - cubic
# O(c^n) - exponential
#   O(2^n)
#   O(3^n)
# O(n!) - factorial
#    SLOW/LARGE

# 445
# https://leetcode.com/problems/add-two-numbers-ii/