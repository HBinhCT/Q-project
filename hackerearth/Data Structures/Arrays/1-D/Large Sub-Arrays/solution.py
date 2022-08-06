from itertools import accumulate

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    sums = list(accumulate(a + a, initial=0))
    total = sums[n]
    if total == k:
        ans = m * n * (n + 1) // 2 + (m - 1) * n * (n - 1) // 2
    elif total * m <= k:
        ans = m * n * (m * n + 1) // 2
    else:
        i = 0
        j = 1
        cnt1 = cnt2 = 0
        q, r = divmod(k, total)
        while i <= j < len(sums):
            diff = sums[j] - sums[i]
            if diff <= r:
                if i < n:
                    if j <= n:
                        cnt1 += j - i + q * n
                    else:
                        cnt2 += n - i
                elif i > n:
                    break
                elif i == j:
                    cnt1 += q * n
                j += 1
            else:
                i += 1
        ans = cnt1 * (m - q) + cnt2 * (m - q - 1) + (n * q) * ((n * q) + 1) // 2
    print(ans % 1000000007)
