n = int(input())
a = input().strip()
s1 = a.count('1')
if s1 == 0:
    print(0)
elif a.count('0') == 0:
    print(s1)
else:
    counts = list(map(lambda x: x.count('1'), a.split('0')))
    ans = 0
    for i in range(len(counts) - 1):
        ans = max(ans, counts[i] + counts[i + 1])
    if s1 > ans:
        print(ans + 1)
    else:
        print(ans)
