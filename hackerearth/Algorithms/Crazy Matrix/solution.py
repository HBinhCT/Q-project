"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque


def moves(x, y, size):
    for i in (x - 1, x + 2):
        if 0 <= i < size:
            for j in (y - 1, y + 2):
                if 0 <= j < size:
                    if i != x and j != y:
                        yield i, j


def check_path_row(x, y, adjacency, size):
    visited = {(x, y)}
    if adjacency[x][y] != 1:
        return False
    stack = deque([(x, y)])
    while stack:
        curr_x, curr_y = stack.pop()
        if curr_x == size - 1:
            return True
        for next_x, next_y in moves(curr_x, curr_y, size):
            if (next_x, next_y) not in visited and adjacency[next_x][next_y] == 1:
                visited.add((next_x, next_y))
                stack.append((next_x, next_y))
    return False


def check_path_col(x, y, adjacency, size):
    visited = {(x, y)}
    if adjacency[x][y] != 2:
        return False
    stack = deque([(x, y)])
    while stack:
        curr_x, curr_y = stack.pop()
        if curr_y == size - 1:
            return True
        for next_x, next_y in moves(curr_x, curr_y, size):
            if (next_x, next_y) not in visited and adjacency[next_x][next_y] == 2:
                visited.add((next_x, next_y))
                stack.append((next_x, next_y))
    return False


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))
is_row = False
for col in range(n):
    if check_path_row(0, col, matrix, n):
        is_row = True
        break
is_col = False
for row in range(n):
    if check_path_col(row, 0, matrix, n):
        is_col = True
        break
if is_row:
    if is_col:
        print('AMBIGUOUS')
    else:
        print(1)
elif is_col:
    print(2)
else:
    print(0)
