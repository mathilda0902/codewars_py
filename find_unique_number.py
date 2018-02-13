# find unique number:
# find_uniq([ 3, 10, 3, 3, 3 ]), 10
from collections import Counter
def find_uniq(arr):
    c = Counter(arr)
    n = c.most_common()[1][0]
    return n

def find_uniq(arr):
    c = Counter(arr)
    for k,v in c.items():
        if v == 1:
            return k

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) else b
