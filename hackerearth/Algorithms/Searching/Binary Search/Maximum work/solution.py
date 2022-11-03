from math import ceil


def solve(K, B, N, W, M, S):
    # Write your code here
    W.sort()
    S.sort()
    left = 0
    right = min(N, M)
    res = 0
    while left <= right:
        mid = (left + right) // 2
        x = K
        for i in range(mid):
            try:
                if S[i] > W[N - mid + i]:
                    if x * B < S[i] - W[N - mid + i]:
                        x = -1
                        break
                    x -= ceil((S[i] - W[N - mid + i]) / B)
            except:
                break
        if x == -1:
            right = mid - 1
        else:
            left = mid + 1
            res = mid
    return res


T = int(input())
for _ in range(T):
    K, B = map(int, input().split())
    N = int(input())
    W = list(map(int, input().split()))
    M = int(input())
    S = list(map(int, input().split()))

    out_ = solve(K, B, N, W, M, S)
    print(out_)
