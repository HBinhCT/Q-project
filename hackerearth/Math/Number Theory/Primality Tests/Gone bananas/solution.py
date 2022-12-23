from functools import lru_cache


@lru_cache(maxsize=None)
def solve(N):
    if N <= 3:
        return 'No'
    else:
        if N % 2 == 0 or N % 3 == 0:
            return 'Yes'
        i = 5
        while i * i <= N:
            if N % i == 0 or N % (i + 2) == 0:
                return 'Yes'
            i += 6
        return 'No'


T = int(input())
for _ in range(T):
    N = int(input())

    out_ = solve(N)
    print(out_)
