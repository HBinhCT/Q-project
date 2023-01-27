from collections import defaultdict
from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().strip().split()))
    # c = [int(input()) for _ in range(n)]  # uncomment this line when submit
    tree = defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().strip().split())
        tree[x].append(y)
        tree[y].append(x)
    time = float('inf')
    candle = 0
    heap = []
    heappush(heap, (-c[0], 1))
    visited = {1}
    while heap:
        cx, x = heappop(heap)
        candle += 1
        time = min(time, candle - cx - 1)
        if candle > time:
            time = 0
            break
        for y in tree[x]:
            if y not in visited:
                visited.add(y)
                heappush(heap, (-c[y - 1], y))
    print(time - candle + 1 if time else 0)
