from math import log


def solve(n):
    # Write your code here
    x = log(n, 2)
    if x == int(x):
        return n
    return (n - 2 ** int(x)) * 2


T = int(input())
for _ in range(T):
    n = int(input())

    out_ = solve(n)
    print(out_)
