from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    strengths = list(map(int, input().strip().split()))
    alive_monsters = deque([])
    counts = []
    for i in strengths:
        while alive_monsters and alive_monsters[-1] <= i:
            alive_monsters.pop()
        alive_monsters.append(i)
        counts.append(len(alive_monsters))
    print(*counts)
