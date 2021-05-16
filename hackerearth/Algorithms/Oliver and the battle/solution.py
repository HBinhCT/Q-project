"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def bazooka(x, y, mapping):
    queue = [(x, y)]
    ans = 0
    while queue:
        u, v = queue.pop()
        for du, dv in directions:
            new_u = u + du
            new_v = v + dv
            if mapping[new_u][new_v]:
                mapping[new_u][new_v] = False
                queue.append((new_u, new_v))
                ans += 1
    return ans


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    battle_ground = [[0] * (m + 2) for _ in range(n + 2)]
    for row in range(1, n + 1):
        battle_ground[row][1:m + 1] = map(int, input().strip().split())
    positions = [[False] * (m + 2) for _ in range(n + 2)]
    for row in range(n + 2):
        for col in range(m + 2):
            if battle_ground[row][col]:
                positions[row][col] = True
    troops = 0
    max_troop = 0
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if positions[row][col]:
                soldiers = bazooka(row, col, positions)
                troops += 1
                max_troop = max(max_troop, soldiers)
    print(troops, max_troop)
