"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
m = int(input())


def find(x, par):
    if par[x] == x:
        return x
    par[x] = find(par[x], par)
    return par[x]


def union(a, b, par, sz):
    a = find(a, par)
    b = find(b, par)
    if a == b:
        return
    if sz[a] > sz[b]:
        par[b] = a
        sz[a] += sz[b]
    else:
        par[a] = b
        sz[b] += sz[a]


parents = [i for i in range(n + 1)]
size = [1] * n
for _ in range(m):
    k = int(input())
    subgroup = list(map(lambda x: int(x) - 1, input().strip().split()))
    u = subgroup[0]
    for v in subgroup[1:]:
        union(u, v, parents, size)
for i in range(n):
    print(size[find(i, parents)], end=' ')
