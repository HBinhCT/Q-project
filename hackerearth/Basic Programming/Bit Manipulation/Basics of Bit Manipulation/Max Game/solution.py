from math import log2


def solve(N):
    # Write your code here
    return 2 ** int(log2(N))


T = int(input())
for _ in range(T):
    N = int(input())

    out_ = solve(N)
    print(out_)
