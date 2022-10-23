from collections import deque
from heapq import heappush, heappop


def bfs(adj, size, start_coordinate, end_coordinate):
    start_x, start_y = start_coordinate
    end_x, end_y = end_coordinate
    moves = ((-1, 0), (0, -1), (0, 1), (1, 0))
    queue = deque([(start_x, start_y, 0)])
    visited = {(start_x, start_y)}
    while queue:
        x, y, w = queue.popleft()
        if x == end_x and y == end_y:
            return w
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited:
                if adj[nx][ny] != '#':
                    queue.append((nx, ny, w + 1))
                visited.add((nx, ny))
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    players = []
    mines = []
    for i in range(n):
        matrix.append(input().strip())
        for j in range(n):
            if matrix[i][j] == '^':
                players.append((i, j))
            elif matrix[i][j] == '*':
                mines.append((i, j))
    dists = []
    for player in players:
        for mine in mines:
            dists.append(bfs(matrix, n, player, mine))
    both_mines = bfs(matrix, n, mines[0], mines[1])
    times = []
    if dists[0] != -1 and dists[3] != -1:
        heappush(times, max(dists[0], dists[3]))
    if dists[1] != -1 and dists[2] != -1:
        heappush(times, max(dists[1], dists[2]))
    if both_mines != -1:
        for dist in dists:
            if dist != -1:
                heappush(times, dist + both_mines)
    if times:
        print('Yes')
        print(heappop(times))
    else:
        print('No')
