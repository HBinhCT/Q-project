from sys import stdin

n, k = map(int, stdin.readline().strip().split())
memory = []
for _ in range(n):
    memory.append(list(map(int, stdin.readline().strip().split())))
q = int(stdin.readline())
for _ in range(q):
    x = int(stdin.readline())
    i = 0
    j = k - 1
    found = 0
    while i < n:
        if memory[i][j] < x:
            i += 1
        elif memory[i][j] > x:
            j -= 1
        else:
            print(i, j)
            break
    else:
        print(-1, -1)
