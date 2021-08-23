"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque

n, m = map(int, input().strip().split())
matrix = []
for _ in range(n):
    matrix.append(input().strip())
move_types = {
    'RD': 'RD',
    'DR': 'DR',
}


def find_path(adjacency, rows, cols, move_type):
    if adjacency[0][0] == '#' or adjacency[rows - 1][cols - 1] == '#':
        return None
    path = set()
    visited = set()
    stack = deque([(0, 0)])
    while stack:
        cell = stack.pop()
        if cell not in visited:
            visited.add(cell)
            path.add(cell)
            if cell == (rows - 1, cols - 1):
                return path
            row, col = cell
            sub_stack = []
            # move down
            next_row = row + 1
            if next_row < rows and adjacency[next_row][col] == '.' and (next_row, col) not in visited:
                sub_stack.append((next_row, col))
            # move right
            next_col = col + 1
            if next_col < cols and adjacency[row][next_col] == '.' and (row, next_col) not in visited:
                sub_stack.append((row, next_col))
            if move_type == move_types['RD']:
                # move right first if possible, then down if possible (stack in opposite order)
                stack.extend(sub_stack)
            elif move_type == move_types['DR']:
                # move down first if possible, then right if possible (stack in opposite order)
                sub_stack.reverse()
                stack.extend(sub_stack)
        else:
            path.remove(cell)
    return None


def determine(adjacency, rows, cols):
    if adjacency[0][0] == '#':
        return None
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        cell = queue.popleft()
        if cell not in visited:
            visited.add(cell)
            row, col = cell
            # move down
            next_row = row + 1
            if next_row < rows and adjacency[next_row][col] == '.' and (next_row, col) not in visited:
                queue.append((next_row, col))
            # move right
            next_col = col + 1
            if next_col < cols and adjacency[row][next_col] == '.' and (row, next_col) not in visited:
                queue.append((row, next_col))
    return visited


def determine_reverse(adjacency, rows, cols):
    # (reverse) explore from (n - 1, m - 1) and return the set of nodes discovered
    if adjacency[rows - 1][cols - 1] == '#':
        return None
    visited = set()
    queue = deque([(rows - 1, cols - 1)])
    while queue:
        cell = queue.popleft()
        if cell not in visited:
            visited.add(cell)
            row, col = cell
            # move up
            next_row = row - 1
            if next_row >= 0 and adjacency[next_row][col] == '.' and (next_row, col) not in visited:
                queue.append((next_row, col))
            # move left
            next_col = col - 1
            if next_col >= 0 and adjacency[row][next_col] == '.' and (row, next_col) not in visited:
                queue.append((row, next_col))
    return visited


ans_lines = []
path_rd = find_path(matrix, n, m, move_types['RD'])
if path_rd:
    ans_lines = [['1'] * m for _ in range(n)]
    path_dr = find_path(matrix, n, m, move_types['DR'])
    for field in path_rd:
        if field in path_dr:
            x, y = field
            ans_lines[x][y] = '0'
else:
    ans_lines = [['0'] * m for _ in range(n)]
    check_list = determine(matrix, n, m)
    check_list_reverse = determine_reverse(matrix, n, m)
    if not check_list and check_list_reverse:
        # (0, 0) is '#'
        if (n > 1 and (1, 0) in check_list_reverse) or (m > 1 and (0, 1) in check_list_reverse):
            ans_lines[0][0] = '1'
    elif check_list and not check_list_reverse:
        # (n - 1, m - 1) is '#'
        if (n > 1 and (n - 2, m - 1) in check_list) or (m > 1 and (n - 1, m - 2) in check_list):
            ans_lines[n - 1][m - 1] = '1'
    elif check_list and check_list_reverse:
        for x in range(n):
            for y in range(m):
                if (x, y) not in check_list and (x, y) not in check_list_reverse:
                    if ((x > 0 and (x - 1, y) in check_list) or (y > 0 and (x, y - 1) in check_list)) and (
                            (x < n - 1 and (x + 1, y) in check_list_reverse) or (
                            y < m - 1 and (x, y + 1) in check_list_reverse)):
                        ans_lines[x][y] = '1'
for ans in ans_lines:
    print(*ans)
