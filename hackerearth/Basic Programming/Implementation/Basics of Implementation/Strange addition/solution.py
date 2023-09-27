t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    a = a[::-1]
    b = b[::-1]
    a = int(a)
    b = int(b)
    c = str(a + b)
    c = int(c[::-1])
    print(c)
