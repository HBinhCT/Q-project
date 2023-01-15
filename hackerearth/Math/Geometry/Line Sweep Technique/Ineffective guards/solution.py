from sys import stdin

n, m = map(int, stdin.readline().strip().split())
guards = []
for _ in range(n):
    x, y = map(int, stdin.readline().strip().split())
    guards.append((y - x, y + x))
guards.sort(key=lambda z: (-z[0], -z[1]))
jewelries = []
for _ in range(m):
    x, y = map(int, stdin.readline().strip().split())
    jewelries.append((y - x, y + x))
jewelries.sort(key=lambda z: -z[0])
ineffective = 0
can_remove = False
increasing = True
cur_sight = next_sight = prev_sight = float('inf')
i = j = 0
while i < n:
    if guards[i][1] >= cur_sight:
        if increasing:
            next_sight = min(prev_sight, guards[i][1])
            increasing = False
        else:
            next_sight = min(next_sight, guards[i][1])
        ineffective += 1
        if i < n - 1:
            while jewelries[j][0] > guards[i + 1][0]:
                if jewelries[j][1] < next_sight:
                    can_remove = False
                j += 1
        else:
            while j < m:
                if jewelries[j][1] < next_sight:
                    can_remove = False
                j += 1
        i += 1
    else:
        increasing = True
        if can_remove:
            ineffective += 1
        can_remove = True
        if i < n - 1:
            while jewelries[j][0] > guards[i + 1][0]:
                if jewelries[j][1] < cur_sight:
                    can_remove = False
                j += 1
        else:
            while j < m:
                if jewelries[j][1] < cur_sight:
                    can_remove = False
                j += 1
        cur_sight, prev_sight = guards[i][1], cur_sight
        i += 1
if can_remove:
    ineffective += 1
print(ineffective)
