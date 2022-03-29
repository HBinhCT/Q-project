from heapq import heappush, heappop

mod = 1000000007
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
n = int(input())
matrix = []
heap = []
for i in range(n):
    matrix.append(list(map(int, input().strip().split())))
    for j in range(n):
        heappush(heap, (-matrix[i][j], i, j))
paths = [[1] * n for _ in range(n)]
while heap:
    h, i, j = heappop(heap)
    for dx, dy in moves:
        x = i + dx
        y = j + dy
        if 0 <= x < n and 0 <= y < n and matrix[x][y] < -h:
            paths[x][y] += paths[i][j]
            paths[x][y] %= mod
ans = 0
for i in range(n):
    ans += sum(paths[i])
    ans %= mod
print(ans)
