t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().strip().split()))
    j = 0
    ans = ''
    for i in p:
        if i == j == 0:
            print(-1)
            break
        elif i == j:
            ans += 'a'
        elif i == j + 1:
            ans += chr(96 + i)
            j += 1
        else:
            print(-1)
            break
    else:
        print(ans)
