from typing import List, Set


def is_match(u, adj, matches, visited=None):
    if visited is None:
        visited = set()
    for v in adj[u] - visited:
        visited.add(v)
        if v not in matches or is_match(matches[v], adj, matches, visited):
            matches[v] = u
            return True
    return False


n, m = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
if len(numbers) != n:
    for _ in range(n - 1):
        numbers.append(int(input()))
divides: List[Set[float]] = [{1} for _ in range(n)]
for i in range(n):
    a = numbers[i]
    if a < m:
        divides[i].add(a)
    for j in range(2, min(m, int(a ** 0.5)) + 1):
        if a % j == 0:
            divides[i].add(j)
            c = a / j
            if c <= m:
                divides[i].add(c)
ans = 0
res = {}
for i in range(n):
    if is_match(i, divides, res):
        ans += 1
print(ans)
