def solve(N, K, chocolates):
    # write your code here
    # return your answer
    ans = set()
    for i in chocolates:
        ans.update(i[1:])
    return 'Yes' if len(ans) >= K else 'No'


T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split(' ')))
    chocolates = []
    for _ in range(N):
        chocolates.append(input().split(' '))
    out_ = solve(N, K, chocolates)
    print(out_)
