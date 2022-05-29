n = int(input())
a = list(map(int, input().strip().split()))
total = sum(a)
count = 0
s1 = s2 = s3 = s4 = 0
for i in range(n):
    count += a[i]
    if count > total // 2:
        s1 = count - a[i]
        s2 = total - s1
        s3 = count
        s4 = total - s3
        break
print(max(s1 * s2, s3 * s4))
