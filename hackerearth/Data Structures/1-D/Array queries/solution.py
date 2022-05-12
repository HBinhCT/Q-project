def array_queries(N, M, A, B, Q, queries):
    # Write your code here
    mod = 998244353
    s1 = sum(A)
    s2 = sum(B)
    s3 = sum((i + 1) * A[i] for i in range(N))
    s4 = sum((i + 1) * B[i] for i in range(M))
    res = [(s1 * s4 + s2 * s3) % mod]
    for tp, i, j in queries:
        i -= 1
        j -= 1
        if tp == 1:
            s1 += B[j] - A[i]
            s2 += A[i] - B[j]
            s3 += (i + 1) * (B[j] - A[i])
            s4 += (j + 1) * (A[i] - B[j])
            A[i], B[j] = B[j], A[i]
        elif tp == 2:
            s3 += (i - j) * (A[j] - A[i])
            A[i], A[j] = A[j], A[i]
        else:
            s4 += (i - j) * (B[j] - B[i])
            B[i], B[j] = B[j], B[i]
        res.append((s1 * s4 + s2 * s3) % mod)
    return res


T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for i in range(Q)]

    out_ = array_queries(N, M, A, B, Q, queries)
    print(' '.join(map(str, out_)))
