def solve(S, k):
    # Write your code here
    return S.count(k)


T = int(input())
for _ in range(T):
    S = input()
    k = input()

    out_ = solve(S, k)
    print(out_)
