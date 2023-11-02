t = int(input())
for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    if set(s1) & set(s2):
        print("Yes")
    else:
        print("No")
