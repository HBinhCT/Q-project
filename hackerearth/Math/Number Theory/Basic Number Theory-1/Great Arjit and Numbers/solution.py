from sys import stdin

mod = 1000000007
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split()))
    ans = 0
    for i in range(1, n):
        val = arr[i] * pow(arr[i - 1], mod - 2, mod) % mod
        ans += val * (val + 1) // 2 % mod
    ans = ans * (ans + 1) // 2 % mod
    print(ans)
