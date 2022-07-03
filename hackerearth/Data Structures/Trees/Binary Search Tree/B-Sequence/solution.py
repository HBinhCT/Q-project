from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().strip().split()))
q = int(stdin.readline())
max_element = max(a)
k = a.index(max_element)
increasing_part = set(a[:k])
decreasing_part = set(a[k + 1:])
for _ in range(q):
    val = int(stdin.readline())
    if val > max_element:
        increasing_part.add(max_element)
        max_element = val
        n += 1
    elif val in increasing_part:
        if val not in decreasing_part:
            decreasing_part.add(val)
            n += 1
    elif val != max_element:
        increasing_part.add(val)
        n += 1
    print(n)
increasing_part = sorted(increasing_part)
decreasing_part = sorted(decreasing_part, reverse=True)
print(*increasing_part, max_element, *decreasing_part)
