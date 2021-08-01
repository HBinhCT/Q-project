"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))


def escape(x, y, size, adjacency, seen):
    if x == size - 1 and y == size - 1:
        global count
        count += 1
        return
    seen[x][y] = True
    for mx, my in moves:
        nx = x + mx
        ny = y + my
        if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny] and not adjacency[nx][ny]:
            escape(nx, ny, size, adjacency, seen)
    seen[x][y] = False
    return


for _ in range(t):
    n = int(input())
    prison = []
    for _ in range(n):
        prison.append(list(map(int, input().strip().split())))
    visited = [[False] * n for _ in range(n)]
    count = 0
    escape(0, 0, n, prison, visited)
    print(count)
