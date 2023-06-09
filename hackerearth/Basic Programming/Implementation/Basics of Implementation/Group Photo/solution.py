def solve(dim):
    # Write your code here
    h = sorted(x[1] for x in dim)
    s = sum(x[0] for x in dim)
    m1 = h[-1]
    m2 = h[-2]
    ans = []
    for i, x in enumerate(dim):
        if x[1] == m1:
            ans.append(m2 * (s - x[0]))
        else:
            ans.append(m1 * (s - x[0]))
    return ans


n = int(input())
dim = []
for _ in range(n):
    dim.append(list(map(int, input().split())))

out_ = solve(dim)
print(' '.join(map(str, out_)))
