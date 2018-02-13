# Fibonacci prod:
import math
phi = (1 + math.sqrt(5)) / 2.
prod = 714

def productFib(prod):
    a, b = 0, 1
    while prod > a*b:
        a, b = b, a+b
    return [a, b, a*b == prod]
