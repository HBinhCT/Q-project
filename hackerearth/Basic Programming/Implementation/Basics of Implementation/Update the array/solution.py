def minUpdates(N, A, K):
    # write your code here
    if N % 2:
        return -1
    uniq_a = sorted(set(A))
    a = b = N // 2
    c = (K + 1) // 2
    d = K // 2
    for x in uniq_a:
        if x % 2:
            a -= 1
            if x <= K:
                c -= 1
        else:
            b -= 1
            if x <= K:
                d -= 1
    x = max(0, b)
    y = max(0, a)
    if x <= d and y <= c:
        return x + y
    else:
        return -1


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = minUpdates(N, A, K)
    print(out_)
