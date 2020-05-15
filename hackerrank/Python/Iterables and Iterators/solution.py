from itertools import combinations

_, s, k = input(), input().rstrip().split(), int(input())
t = list(combinations(s, k))
f = list(filter(lambda c: 'a' in c, t))
print(len(f) / len(t))
