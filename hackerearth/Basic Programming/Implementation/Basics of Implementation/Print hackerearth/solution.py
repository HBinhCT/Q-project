n = int(input())
s = input().strip()
h = s.count('h') // 2
a = s.count('a') // 2
c = s.count('c')
k = s.count('k')
e = s.count('e') // 2
r = s.count('r') // 2
t = s.count('t')
print(sorted((h, a, c, k, e, r, t))[0])
