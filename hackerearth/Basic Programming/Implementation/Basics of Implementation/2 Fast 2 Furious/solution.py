n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
v1 = max(abs(a[i + 1] - a[i]) for i in range(n - 1))
v2 = max(abs(b[i + 1] - b[i]) for i in range(n - 1))
if v1 == v2:
    print("Tie")
elif v1 > v2:
    print("Dom")
    print(v1)
else:
    print("Brian")
    print(v2)
