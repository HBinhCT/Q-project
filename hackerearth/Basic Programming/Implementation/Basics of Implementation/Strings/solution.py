t = int(input())
for _ in range(t):
    n, m = input().strip().split()
    if n == m or (n, m) in (("2", "4"), ("4", "2")):  # n ^ m = m ^ n
        print("YES")
    else:
        print("NO")
