n = int(input())
m = int(input())
r = input().strip()
rg = r.count('G')
rc = r.count('C')
interactions = []
for _ in range(n):
    l = int(input())
    s = input().strip()
    interactions.append(rg * s.count('C') + s.count('G') * rc)
print(interactions.index(max(interactions)) + 1)
