from sys import stdin
from collections import Counter

mod = 1000000007
n = int(stdin.readline())
total_courses = size = 0
faculty_courses = []
lvl_counter = []
for n_ in range(n):
    m, *x = list(map(int, stdin.readline().strip().split()))
    total_courses += m
    if m > 1:
        faculty_courses.append(m)
        for v in Counter(x).values():
            if v > 1:
                lvl_counter.append(v)
if faculty_courses:
    size = max(faculty_courses)
if lvl_counter:
    size = max(size, *lvl_counter)
size = max(size, total_courses)
comp = [1, 1]
for i in range(2, size + 1):
    comp.append(comp[i - 1] * i % mod)
ans = comp[total_courses]
for i in faculty_courses:
    ans = ans * pow(comp[i], mod - 2, mod) % mod
for i in lvl_counter:
    ans = ans * comp[i] % mod
print(ans)
