from heapq import heappush, heapreplace
from sys import stdin

c, p, n = map(int, stdin.readline().strip().split())
y = list(map(int, stdin.readline().strip().split()))
x = list(map(int, stdin.readline().strip().split()))
x.extend([0] * (p - len(x)))
heap = []
for i in range(n):
    heappush(heap, (y[i], i + 1, 1, y[i], 0))
for i in range(n, c):
    heappush(heap, (0, i + 1, 0, 0, 0))
for i in x:
    _, course_id, enrolled, last1, _ = heap[0]
    print(course_id, end=' ')
    enrolled += 1
    last2 = last1
    last1 = i
    heapreplace(heap, (enrolled * (last1 + last2), course_id, enrolled, last1, last2))
