from sys import stdin

n = int(stdin.readline())
strings = []
for _ in range(n):
    strings.append(stdin.readline().strip())
strings.sort()
nodes = len(strings[0])
for i in range(1, n):
    s1 = strings[i - 1]
    s2 = strings[i]
    l1 = len(s1)
    l2 = len(s2)
    m = min(l1, l2)
    j = 0
    while j < m and s1[j] == s2[j]:
        j += 1
    nodes += l2 - j
print(nodes + 1)
