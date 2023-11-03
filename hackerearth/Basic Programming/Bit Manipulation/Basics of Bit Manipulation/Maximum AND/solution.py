t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    val = b - 1 if b & 1 else b - 2
    print(val if val >= a else a & b)
