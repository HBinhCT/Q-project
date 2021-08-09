"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
mod = 1000000007


def find(i, p):
    if p[i] == i:
        return i
    p[i] = p[p[i]]
    return find(p[i], p)


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    relationship = []
    for _ in range(m):
        relationship.append(list(map(int, input().strip().split())))
    relationship.sort(key=lambda x: x[-1])
    parents = list(range(n))
    counter = [1] * n
    res = 1
    for a, b, c in relationship:
        x = find(a - 1, parents)
        y = find(b - 1, parents)
        if parents[x] != parents[y]:
            if counter[x] > counter[y]:
                parents[y] = x
                counter[x] += counter[y]
            else:
                parents[x] = y
                counter[y] += counter[x]
            res *= c
            res %= mod
    print(res)
