def solve(N, S):
    # Write your code here
    s1 = ''
    s2 = ''
    for c in S:
        if s1 == '':
            s1 += c
        elif s1[-1] != c:
            s1 += c
        elif s2 == '':
            s2 += c
        elif s2[-1] != c:
            s2 += c
    return len(s1) + len(s2) - 1 - (s2 != '')


T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    out_ = solve(N, S)
    print(out_)
