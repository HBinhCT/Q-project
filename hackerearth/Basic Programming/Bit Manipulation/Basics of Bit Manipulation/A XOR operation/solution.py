from functools import reduce
from operator import xor


def find_k(e):
    res = reduce(xor, e)
    if not res:
        return -1
    e = set(e)
    if all(res ^ i in e for i in e):
        return res
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().strip().split()))
    print(find_k(s))
