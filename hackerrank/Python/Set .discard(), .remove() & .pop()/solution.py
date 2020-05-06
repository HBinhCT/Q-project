n = int(input())
s = set(map(int, input().split()))

N = int(input())
for _ in range(N):
    method, *args = input().split()
    getattr(s, method)(*map(int, args))
print(sum(s))
