mod = 1000000007


def count(x, y, z):
    w = z * 2
    u = x + w - x % w
    v = y + w - y % w
    return min(u - x, z) - min(v - y - 1, z) + (v - u) // 2


n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().strip().split())
    ans = 0
    r1 = b - a + 1
    r2 = d - c + 1
    for i in range(max(b, d).bit_length()):
        p = pow(2, i)
        on1 = count(a, b, p)
        on2 = count(c, d, p)
        off1 = r1 - on1
        off2 = r2 - on2
        ans += (on1 * off2 % mod + on2 * off1 % mod) * p % mod
        ans %= mod
    print(ans)
