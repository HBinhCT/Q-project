def query(arr, lim, val):
    idx = lim - val + 1
    res = 0
    while idx:
        res = max(res, arr[idx])
        idx -= idx & -idx
    return res


def update(arr, lim, val, base):
    if val > 0:
        idx = lim + 1 - val
        while idx <= lim:
            arr[idx] = max(arr[idx], base)
            idx += idx & -idx


n, h = map(int, input().strip().split())
members = []
for _ in range(n):
    members.append(tuple(map(int, input().strip().split())))
members.sort()
m1 = m2 = 0
for _, x in members:
    if x < 0:
        m1 = max(m1, h + x)
        m2 = max(m2, -x)
    else:
        m1 = max(m1, x)
        m2 = max(m2, h - x)
dp1 = [0] * (m1 + 1)
dp2 = [0] * (m2 + 1)
throws = [0] * n
i = 0
while i < n:
    j = i
    while j < n and members[i][0] == members[j][0]:
        j += 1
    k = i
    while k < j:
        _, x = members[k]
        if x < 0:
            throws[k] = query(dp2, m2, -x)
        else:
            throws[k] = query(dp1, m1, x)
        k += 1
    while i < j:
        _, x = members[i]
        if x < 0:
            update(dp1, m1, h + x, throws[i] + 1)
        else:
            update(dp2, m2, h - x, throws[i] + 1)
        i += 1
print(max(throws))
