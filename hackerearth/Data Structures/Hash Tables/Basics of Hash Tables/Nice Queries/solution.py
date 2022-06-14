from sys import stdin

n, q = map(int, stdin.readline().strip().split())
k_indexes = {}
last_index = 0
for _ in range(q):
    p, ky = map(int, stdin.readline().strip().split())
    if p == 1:
        k_indexes[ky] = 1
        last_index = max(last_index, ky)
    else:
        if ky > last_index:
            print(-1)
        else:
            for i in range(ky, last_index + 1):
                if i in k_indexes:
                    print(i)
                    break
