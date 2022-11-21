from sys import stdin

mod = 1000003


def fac(arr, i):
    ln = len(arr)
    if i < ln:
        return arr[i]
    for i in range(ln, i + 1):
        arr.append(arr[i - 1] * i % mod)
    return arr[-1]


t = int(stdin.readline())
comp = [1, 1]
for _ in range(t):
    n, x = map(int, stdin.readline().strip().split())
    print(0 if x >= mod else fac(comp, n) * x % mod)
