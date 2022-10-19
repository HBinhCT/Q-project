def solve(N, K, S):
    new_str = S[0]
    i = 1
    while i < N:
        q, r = divmod(N, len(new_str))
        if new_str + S[i:] < (new_str * q + new_str[:r])[:N]:
            new_str += S[i]
            i += 1
        else:
            break
    nk = N + K
    m = nk // len(new_str) + 1
    p = new_str * m
    return p[:nk]


T = int(input())
for _ in range(T):
    N = int(input())
    K = int(input())
    S = input()

    out_ = solve(N, K, S)
    print(out_)
