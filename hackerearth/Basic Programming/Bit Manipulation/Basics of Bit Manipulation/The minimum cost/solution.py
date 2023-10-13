t = int(input())
for _ in range(t):
    n, c01, c10 = map(int, input().strip().split())
    a = input().split()
    s1 = a[0::2]
    s2 = a[1::2]
    w = s1.count("0") * c01
    x = s2.count("0") * c01
    y = s1.count("1") * c10
    z = s2.count("1") * c10
    print(min(w + z, x + y))
