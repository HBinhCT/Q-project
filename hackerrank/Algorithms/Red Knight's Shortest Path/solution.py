#!/bin/python3


# Complete the printShortestPath function below.
def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    # The order of priority: UL, UR, R, LR, LL, L
    # [(row, col, position)] = [(-2, -1, 'UL'), (-2, 1, 'UR'), (0, 2, 'R'), (2, 1, 'LR'), (2, -1, 'LL'), (0, -2, 'L')]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = [[i_start, j_start, 0, []]]
    while queue:
        i_cur, j_cur, count, path = queue.pop(0)
        if visited[i_cur][j_cur] == 0:
            visited[i_cur][j_cur] = 1
            # check if reached
            if i_cur == i_end and j_cur == j_end:
                print(count)
                print(*path)
                return
            # upper
            if i_end < i_cur:
                if j_end == j_start:
                    positions = [(-2, -1, 'UL'), (-2, 1, 'UR')]
                else:
                    positions = [(-2, 1, 'UR'), (0, 2, 'R'), (-2, -1, 'UL'), (0, -2, 'L')]
            # lower
            elif i_end > i_cur:
                if j_end == j_start:
                    positions = [(2, 1, 'LR'), (2, -1, 'LL')]
                else:
                    positions = [(0, 2, 'R'), (2, 1, 'LR'), (2, -1, 'LL'), (0, -2, 'L')]
            # same
            else:
                if j_end < j_start:
                    positions = [(0, -2, 'L')]
                else:
                    positions = [(0, 2, 'R')]
            moves = []
            for move_i, move_j, step in positions:
                if 0 <= i_cur + move_i < n and 0 <= j_cur + move_j < n and 0 == visited[i_cur + move_i][j_cur + move_j]:
                    moves.append([i_cur + move_i, j_cur + move_j, count + 1, path + [step]])
            if moves:
                queue.extend(moves)
    else:
        print('Impossible')


if __name__ == '__main__':
    n = int(input())

    i_startJ_start = input().split()

    i_start = int(i_startJ_start[0])

    j_start = int(i_startJ_start[1])

    i_end = int(i_startJ_start[2])

    j_end = int(i_startJ_start[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
