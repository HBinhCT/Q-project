t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    passengers = []
    for _ in range(n):
        s, e = map(int, input().strip().split())
        passengers.append((s, e))
    passengers = sorted(passengers)
    counter = [0] * 101
    for i in range(n):
        s, e = map(lambda x: x + 1, passengers[i])
        if counter[s] >= m:
            continue
        for j in range(s, e):
            counter[j] += 1
    is_full = False
    revenue = 0
    for i in range(1, 101):
        if counter[i]:
            if 2 == counter[i]:
                revenue += 10 * counter[i] * 0.95
            elif 3 <= counter[i]:
                revenue += 10 * counter[i] * 0.93
            else:
                revenue += 10 * counter[i]
            if counter[i] == m:
                is_full = True
    if is_full:
        print(round(revenue), 'Cab was full')
    else:
        print(round(revenue))
