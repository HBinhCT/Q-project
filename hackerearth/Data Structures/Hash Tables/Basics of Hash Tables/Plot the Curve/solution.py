t = int(input())
for _ in range(t):
    a, b, c, d, m = map(int, input().strip().split())
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = 0
    lhs_arr = []  # left-hand side list
    rhs_arr = []  # right-hand side list
    for i in arr:
        lhs_arr.append((i * i) % m)
        rhs_arr.append((a * i * i * i + b * i * i + c * i + d) % m)
    for i in set(lhs_arr) & set(rhs_arr):
        ans += lhs_arr.count(i) * rhs_arr.count(i)
    print(ans % 1000000007)
