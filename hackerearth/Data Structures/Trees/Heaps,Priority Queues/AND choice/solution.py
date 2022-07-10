n = int(input())
a = sorted(map(int, input().strip().split()))
if n >= 2 and a[0] == a[-1]:
    print(a[0] & a[0])
elif a[-1] - a[0] == 1:
    print(a[-1] & a[0])
else:
    if n >= 3 and a[-2] & a[-1] > a[-3] & a[-2]:
        print(a[-2] & a[-1])
    elif n >= 10:
        max_val = 0
        for i in range(n - 20, n):
            for j in range(i + 1, n):
                max_val = max(max_val, a[i] & a[j])
        print(max_val)
    else:
        print(a[-3] & a[-2])
