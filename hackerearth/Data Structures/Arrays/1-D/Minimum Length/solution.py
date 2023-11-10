t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip().split()
    b = input().strip().split()
    c = [i for i in range(n) if a[i] != b[i]]
    if c:
        print(max(c) - min(c) + 1)
    else:
        print(0)
