primes = [2, 3]
for i in range(2, 50):
    k = int(i ** .5)
    for j in range(2, k + 1):
        if i % j == 0:
            break
        if j == k:
            primes.append(i)
not_killed = {1: [1]}
alive = [1]
for i in range(2, 51):
    if i not in primes:
        not_killed[i] = alive
        continue
    same = alive.copy()
    for j in alive:
        same.append(i * j)
    alive = sorted(same)
    not_killed[i] = alive
t = int(input())
for _ in range(t):
    p, x = map(int, input().strip().split())
    if len(not_killed[p]) >= x:
        print(not_killed[p][x - 1])
    else:
        print(-1)
