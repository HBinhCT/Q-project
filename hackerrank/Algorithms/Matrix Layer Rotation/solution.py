#!/bin/python3


# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    height = len(matrix)
    width = len(matrix[0])
    for i in range(min(height // 2, width // 2)):
        state = []
        # top-left to top-right
        for j in range(i, width - i):
            state.append(matrix[i][j])
        # top-right to bottom-right
        for j in range(i + 1, height - 1 - i):
            # in Python, a[len(a) - 1 - i] = a[-1 - i]
            state.append(matrix[j][-1 - i])
        # bottom-right to bottom-left
        for j in range(width - 1 - i, i - 1, -1):
            state.append(matrix[-1 - i][j])
        # left-bottom to left-top
        for j in range(height - 2 - i, i, -1):
            state.append(matrix[j][i])
        # rotate by R
        # no. of nodes
        no = 2 * (height - 2 * i) + 2 * (width - (2 * i + 2))
        k = r % no
        state = state[k:] + state[:k]
        # populate A with rotated matrix same as above
        flag = 0
        for j in range(i, width - i):
            matrix[i][j] = state[flag]
            flag += 1
        for j in range(i + 1, height - 1 - i):
            matrix[j][-1 - i] = state[flag]
            flag += 1
        for j in range(width - 1 - i, i - 1, -1):
            matrix[-1 - i][j] = state[flag]
            flag += 1
        for j in range(height - 2 - i, i, -1):
            matrix[j][i] = state[flag]
            flag += 1
    for row in matrix:
        print(*row, end=' ')
        print('')


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
