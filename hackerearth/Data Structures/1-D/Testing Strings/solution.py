mod = 1000003
n, m, k = map(int, input().strip().split())
pieces = []
for _ in range(n):
    l, r, z = map(int, input().strip().split())
    pieces.append((z, l, r))
pieces.sort()
counter = [0] * (m + 1)
i = j = 0
while i < n:
    j = i
    end = -1
    while j < n and pieces[i][0] == pieces[j][0]:
        _, left, right = pieces[j]
        left = max(left, end + 1)
        if left <= right:
            counter[left - 1] += 1
            counter[right] -= 1
        end = max(end, right)
        j += 1
    i = j
ans = 1
total = 0
for i in range(m):
    total += counter[i]
    ans *= k - total
    ans %= mod
print(ans)
