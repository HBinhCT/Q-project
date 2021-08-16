"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m = map(int, input().strip().split())


def find(x, p):
    if p[x] == x:
        return x
    res = find(p[x], p)
    p[x] = res
    return res


def union(x, y, p, r):
    px = find(x, p)
    py = find(y, p)
    if px != py:
        if r[px] <= r[py]:
            p[px] = py
            r[py] += 1
        else:
            p[py] = px
            r[px] += 1


men_roads = []
women_roads = []
men = set()
women = set()
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    if c in (1, 3):
        men_roads.append((a, b, c))
        men.add(a)
        men.add(b)
    if c in (2, 3):
        women_roads.append((a, b, c))
        women.add(a)
        women.add(b)
if len(men) != n or len(women) != n:
    print(-1)
else:
    men_roads.sort(key=lambda x: x[-1], reverse=True)
    women_roads.sort(key=lambda x: x[-1], reverse=True)
    possible_roads = set()
    for list_roads in (men_roads, women_roads):
        parents = [i for i in range(n)]
        ranks = [1] * n
        for a, b, c in list_roads:
            find_a = find(a - 1, parents)
            find_b = find(b - 1, parents)
            if find_a != find_b:
                union(find_a, find_b, parents, ranks)
                possible_roads.add((a, b))
    print(m - len(possible_roads))
