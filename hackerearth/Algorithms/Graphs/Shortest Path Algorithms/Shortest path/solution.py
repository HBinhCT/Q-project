from collections import defaultdict
from heapq import heappush, heappop


def solve(N, M, A):
    # Write your code here
    graph = defaultdict(list)
    for u, v, w in A:
        u -= 1
        v -= 1
        graph[u].append((w, v))
    if 0 not in graph:
        return -1
    heap = []
    for w, v in graph[0]:
        heappush(heap, (w, v))
    dist = [-1] * N
    dist[0] = 0
    for i in range(1, N):
        while heap and i > heap[0][1]:
            heappop(heap)
        if not heap:
            return -1
        dist[i] = heap[0][0]
        for w, v in graph[i]:
            heappush(heap, (w + dist[i], v))
    return dist[N - 1]


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(M)]

    out_ = solve(N, M, A)
    print(out_)
