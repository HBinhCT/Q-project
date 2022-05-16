from collections import OrderedDict
from sys import stdin

n = int(input())
a = list(map(int, stdin.readline().strip().split()))
frequencies = OrderedDict()
for i in a:
    if i in frequencies:
        frequencies[i] += 1
    else:
        frequencies[i] = 1
keys = list(frequencies.keys())
values = list(frequencies.values())
unique_values = set(values)
most = max(unique_values)
q = int(input())
for _ in range(q):
    tp, f = map(int, stdin.readline().strip().split())
    if f > most:
        print(0)
    elif tp == 0:
        for i in keys:
            if frequencies[i] >= f:
                print(i)
                break
    elif f in unique_values:
        print(keys[values.index(f)])
    else:
        print(0)
