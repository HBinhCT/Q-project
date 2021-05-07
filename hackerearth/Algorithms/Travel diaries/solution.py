"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque


def get_convert_time(mt, adjacent_cells, convert_cells, rows, cols):
    count = 0
    while True:
        count += 1
        waiting = deque()
        while adjacent_cells:
            i, j = adjacent_cells.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < rows and 0 <= y < cols:
                    if mt[x][y] == 1:
                        mt[x][y] = 2
                        waiting.append((x, y))
                        convert_cells -= 1
        if not waiting:
            break
        adjacent_cells = waiting
    if convert_cells:
        return -1
    return count - 1


n, m = map(int, input().split())
matrix = list()
cells_2 = deque()
count_1 = 0
for _ in range(n):
    try:
        matrix.append(list(map(int, input().split())))
    except EOFError:
        break
for i in range(0, n):
    for j in range(0, m):
        try:
            if matrix[i][j] == 2:
                cells_2.append((i, j))
            elif matrix[i][j] == 1:
                count_1 += 1
        except IndexError:
            continue
try:
    print(get_convert_time(matrix, cells_2, count_1, n, m))
except IndexError:
    print(999)
