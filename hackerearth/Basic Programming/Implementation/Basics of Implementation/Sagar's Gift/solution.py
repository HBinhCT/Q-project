t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip().split()
    b = sorted((i for i in ''.join(a)), reverse=True)
    ans = ''.join(b)
    print(ans)
