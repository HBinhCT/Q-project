#!/bin/python3

MAX_VAL = 999999


def calculate_distances(nodes, r_from, r_to, r_weight):
    dist = [[MAX_VAL] * nodes for _ in range(nodes)]  # 1 <= r <= 350
    for f, t, w in zip(r_from, r_to, r_weight):
        dist[f - 1][t - 1] = w
        dist[f - 1][f - 1] = 0
        dist[t - 1][t - 1] = 0
    for r in range(nodes):
        d_r = dist[r]
        for s in range(nodes):
            if dist[s][r] == MAX_VAL:
                continue
            d_s = dist[s]
            for t in range(nodes):
                if d_r[t] == MAX_VAL:
                    continue
                d_s[t] = min(d_s[t], d_s[r] + d_r[t])
    return dist


def shortest_distance(g, a, b):
    return g[a - 1][b - 1] if g[a - 1][b - 1] != MAX_VAL else -1


if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().split())

    q = int(input())

    dis = calculate_distances(road_nodes, road_from, road_to, road_weight)

    for q_itr in range(q):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])

        result = shortest_distance(dis, x, y)

        print(result)
