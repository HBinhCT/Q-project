n = int(input())
a = list(map(int, input().strip().split()))
print(sum(a[0::3]), sum(a[1::3]), sum(a[2::3]))
