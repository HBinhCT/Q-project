n, k = map(int, input().strip().split())
city_groups = {}
for i in range(1, k + 1):
    s, *cities = map(int, input().strip().split())
    for j in cities:
        city_groups[j] = i
q = int(input())
for _ in range(q):
    x, y = map(int, input().strip().split())
    z = abs(city_groups[x] - city_groups[y])
    print(min(z, k - z))
