def solve(N, S):
    # Write your code here
    import math
    sum1 = sum(int(i) for i in S[:N])
    sum2 = sum(int(i) for i in S[N:])
    return math.ceil(abs(sum1 - sum2) / 9)


T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    out_ = solve(N, S)
    print(out_)
