from bisect import bisect_left
from sys import stdin

s = stdin.readline().strip()
n = int(stdin.readline())
vals = list(map(int, stdin.readline().strip().split()))
vowel_str = ''
counter = [0]
count = 0
for c in s:
    if c in 'aeiou':
        vowel_str += c
        count += 1
    counter.append(count)
m = len(vowel_str)
totals = []
lims = []
total = 0
for val in vals:
    if val < 0:
        total += m - counter[-val]
        totals.append(total)
        lims.append(m)
    else:
        total += counter[val + 1]
        totals.append(total)
        lims.append(counter[val + 1])
q = int(stdin.readline())
k = list(map(int, stdin.readline().strip().split()))
for i in range(q):
    if k[i] > totals[-1]:
        print(-1)
    else:
        j = bisect_left(totals, k[i])
        print(vowel_str[-(m - lims[j] + totals[j] - k[i] + 1)])
