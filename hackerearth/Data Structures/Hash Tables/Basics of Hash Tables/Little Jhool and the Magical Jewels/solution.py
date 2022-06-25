t = int(input())
for _ in range(t):
    s = input().strip()
    counter = {'r': 0, 'u': 0, 'b': 0, 'y': 0}
    for c in s:
        try:
            counter[c] += 1
        except:
            continue
    print(min(counter.values()))
