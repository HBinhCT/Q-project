p, s, t, h, x = map(int, input().strip().split())
total = 0
for _ in range(x):
    if s > t:
        total += p
    else:
        total += h
    s -= 1
print(total)
