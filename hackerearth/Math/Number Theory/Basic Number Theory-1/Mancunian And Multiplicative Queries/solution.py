from collections import defaultdict
from sys import stdin

mod = 1000000007
n, c, q = map(int, stdin.readline().strip().split())
a = list(map(int, stdin.readline().strip().split()))
func = list(map(int, stdin.readline().strip().split()))
queries = []
m = int(n ** 0.5)
for _ in range(q):
    l, r = map(int, stdin.readline().strip().split())
    queries.append(((l - 1) // m, r - 1, l - 1))
increases = func.copy()
decreases = func.copy()
for i in range(n + 1):
    j = pow(func[i], mod - 2, mod)
    if i > 0:
        decreases[i - 1] = decreases[i - 1] * j % mod
    if i < n:
        increases[i + 1] = increases[i + 1] * j % mod
low = 0
high = -1
val = pow(func[0], c, mod)
counter = defaultdict(int)
ans = 1
for _, right, left in sorted(queries):
    while high < right:
        high += 1
        counter[a[high]] += 1
        val = val * increases[counter[a[high]]] % mod
    while high > right:
        counter[a[high]] -= 1
        val = val * decreases[counter[a[high]]] % mod
        high -= 1
    while low < left:
        counter[a[low]] -= 1
        val = val * decreases[counter[a[low]]] % mod
        low += 1
    while low > left:
        low -= 1
        counter[a[low]] += 1
        val = val * increases[counter[a[low]]] % mod
    ans = ans * val % mod
print(ans)
