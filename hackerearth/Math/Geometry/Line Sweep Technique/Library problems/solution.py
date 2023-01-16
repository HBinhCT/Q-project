n, r = map(int, input().strip().split())
tables = [list(map(int, input().strip().split())) for _ in range(n)]
print(n)
for i in tables:
    print(*i)
