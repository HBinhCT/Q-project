days = []
for _ in range(7):
    days.append(sum(map(int, input().strip())))
ans = 0
avg = sum(days) / 7
for day in days:
    ans += (day - avg) ** 2
ans = (ans / 7) ** 0.5
print(f"{ans:.4f}")
