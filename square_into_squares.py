# Square into Squares. Protect trees!
# Given a positive integral number n, return a strictly increasing sequence
# (list/array/string depending on the language) of numbers, so that the sum of
# the squares is equal to n².
# If there are multiple solutions (and there will be), return the result with
# the largest possible values:

# test cases:
# decompose(5), [3,4]
#
# decompose(11) must return [1,2,4,10]. Note that there are actually two ways to
# decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't
# return [2,6,9], since 9 is smaller than 10.
#
# For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since
# [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

def decompose(n):
    n = 50
    rem = n ** 2
    x = n - 1
    lst = [x ** 2]
    output = [x]
    while x >= 1:
        rem -= x ** 2
        x = int(rem ** 0.5)
        lst.append(x ** 2)
        output.append(x)
        if x == 0:
            output.pop(-1)
    print sorted(output)

    if n ** 2 == sum(lst):
        return sorted(lst)




















if __name__ == '__main__':
    pass
