t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    for i in range(n):
        if a[i] == b[i] == 0 or a[i] + b[i] != 0:
            print('Yes' if sum(a) == sum(b) else 'No')
            break
    else:
        print('No')
