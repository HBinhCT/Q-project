t = int(input())
for _ in range(t):
    z, n = map(int, input().strip().split())
    s = list(map(int, input().strip().split()))
    for i in s:
        z = z & i
        if not z:
            print("Yes")
            break
    else:
        print("No")
