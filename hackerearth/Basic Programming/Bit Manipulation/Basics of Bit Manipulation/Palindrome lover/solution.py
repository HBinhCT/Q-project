t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    if not n % 2 and sum(map(lambda x: x % 2, a)) % 2:
        print(0)
    else:
        print(1)
