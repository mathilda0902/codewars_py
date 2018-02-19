# Write a program that will calculate the number of trailing zeros in a factorial of
# a given number.
#
# N! = 1 * 2 * 3 * ... * N
#
# Be careful 1000! has 2568 digits...
#
# For more info, see: http://mathworld.wolfram.com/Factorial.html
#
# Examples
#
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
#
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way to find the
# number of zeros.

#version 1
import math

def zeros(n):
    z = 0
    if n > 0:
        km = math.floor(math.log(n, 5)) + 1
        for k in range(1, km):
            z += math.floor( n / (5 ** k))
    return z

# version 2
def zeros(n):
    x = n // 5
    return x + zeros(x) if x else 0
