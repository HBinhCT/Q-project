from collections import defaultdict
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    top_spends = defaultdict(list)
    for _ in range(n):
        s, x = stdin.readline().strip().split()
        x = int(x)
        top_spends[s].append(x)
        if len(top_spends[s]) > 1:
            top_spends[s] = sorted(top_spends[s])[-3:]
    most_spent = 0
    festival_name = ''
    for s, x in top_spends.items():
        total = sum(x)
        if total > most_spent:
            most_spent = total
            festival_name = s
        elif total == most_spent and s < festival_name:
            festival_name = s
    print(festival_name, most_spent)
