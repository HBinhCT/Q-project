n = int(input())
for _ in range(n):
    s = input().strip()
    print("YES" if 26 == len(set(s)) else "NO")
