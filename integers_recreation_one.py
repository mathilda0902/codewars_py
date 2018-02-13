# Integers: Recreation One
# Given two integers m, n (1 <= m <= n) we want to find all integers between
# m and n whose sum of squared divisors is itself a square. 42 is such a number.
# return list_squared(42, 250) --> [[42, 2500], [246, 84100]]
def is_squared(n):
    if n ** 0.5 ==  int(n ** 0.5):
        return True
    else:
        return False

def divisors_squared(n):
    div_sq = []
    for p in xrange(1, int(n ** 0.5 + 1)):
        if n % p == 0:
            div_sq.extend([p ** 2, (n/p) ** 2])
    return sorted(set(div_sq))

def list_squared(m, n):
    output = []
    for x in xrange(m, n+1):
        summation = sum(divisors_squared(x))
        if is_squared(summation):
            output.append([x, summation])
    return output

%time list_squared(250, 500)
#[[287, 84100]]
list_squared(42, 250)
#[[42, 2500], [246, 84100]]
list_squared(1, 250)
#[[1, 1], [42, 2500], [246, 84100]]
