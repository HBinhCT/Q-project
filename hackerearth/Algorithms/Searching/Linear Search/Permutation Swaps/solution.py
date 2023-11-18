t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    if 2 * sum(a) != n * (n + 1):
        print("NO")
    else:
        j = 0
        for i, v in enumerate(a):
            j += v - i - 1
            if j < 0:
                print("NO")
                break
        else:
            print("YES")
