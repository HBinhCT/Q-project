n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
j = a.index(min(a))
steps = 0
while a[j] >= b[j]:
    for i in range(n):
        if a[i] != a[j]:
            x = a[i] - a[j]
            if x % b[i]:
                break
            else:
                steps += x // b[i]
    else:
        print(steps)
        break
    a[j] -= b[j]
    steps += 1
else:
    print(-1)
