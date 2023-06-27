t = int(input())
for _ in range(t):
    a, n = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    for i in range(n):
        if a:
            if arr[i]:
                a += 2
            else:
                a -= 1
        else:
            print('No', i)
            break
    else:
        print('Yes', a)
