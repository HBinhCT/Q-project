n, l, m = map(int, input().strip().split())
packages = list(map(int, input().strip().split()))
choose = 0
for i in range(m):
    if packages[i] > l:
        choose += 1
ways = int(not choose)
for i in range(m, n):
    if packages[i] > l:
        choose += 1
    if packages[i - m] > l:
        choose -= 1
    ways += not choose
print(ways)
