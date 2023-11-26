t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input()
    if k > n or k > len(set(s)):
        print("NO")
    else:
        print("YES")
