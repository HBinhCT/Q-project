from math import lcm

t = int(input())
mod = 1000000007
for _ in range(t):
    n = int(input())
    room = list(map(int, input().split()))
    if len(set(room)) != n:
        print(-1)
        continue
    visited = set()
    k = 1
    for i in range(1, n + 1):
        if i not in visited:
            seen = set()
            j = i
            while j not in seen:
                seen.add(j)
                j = room[j - 1]
            k = lcm(k, len(seen))
            k %= mod
            visited.update(seen)
    print(k)
