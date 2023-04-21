t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    print(max(a, b) // min(a, b))
