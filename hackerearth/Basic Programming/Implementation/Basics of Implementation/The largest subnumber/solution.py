def largest_sol(N, K, S):
    # Write your code here
    S = list(map(int, S))
    a = [S[0]] * N
    b = [1] * N
    for i in range(1, N):
        a[i] = a[i - 1] ^ S[i]
        j = N - i - 1
        b[j] = b[j + 1] * 10 % K
    x = -1
    y = z = 0
    for i in range(N - 1, 0, -1):
        z = (z + S[i] * b[i]) % K
        if S[i] and not z and x <= a[i - 1]:
            y = i
            x = a[i - 1]
    return x if x == -1 else ''.join(map(str, S[y:]))


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input()

    out_ = largest_sol(N, K, S)
    print(out_)
