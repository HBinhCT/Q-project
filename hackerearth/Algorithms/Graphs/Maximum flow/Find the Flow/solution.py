from collections import deque


def bfs(graph, source, sink, parents):
    parents[source] = -1
    visited = [False] * 26
    visited[source] = True
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in range(26):
            if not visited[v] and graph[u][v]:
                visited[v] = True
                queue.appendleft(v)
                parents[v] = u
    return visited[sink]


def ford_fulkerson(graph, source, sink):
    parents = [0] * 26
    max_flow = 0
    while bfs(graph, source, sink, parents):
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parents[v]
            path_flow = min(path_flow, graph[u][v])
            v = parents[v]
        v = sink
        while v != source:
            u = parents[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parents[v]
        max_flow += path_flow
    return max_flow


e = int(input())
network = [[0] * 26 for _ in range(26)]
for _ in range(e):
    vi, vj, cx = input().strip().split()
    cx = int(cx)
    vi = ord(vi) - 65  # 65 is ord('A')
    vj = ord(vj) - 65
    network[vi][vj] = cx
print(ford_fulkerson(network, ord('S') - 65, ord('T') - 65))
