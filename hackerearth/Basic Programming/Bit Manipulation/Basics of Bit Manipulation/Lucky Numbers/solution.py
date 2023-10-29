from bisect import bisect_right

lucky_numbers = []
for i in range(59):
    x = 1 << i
    for j in range(i + 1, 60):
        lucky_numbers.append((x | 1 << j))
lucky_numbers.sort()
mod = 1000000007
ln = len(lucky_numbers)
sums = [0] * ln
sums[0] = 3
for i in range(1, ln):
    sums[i] = (sums[i - 1] + lucky_numbers[i]) % mod
t = int(input())
for i in range(t):
    n = int(input())
    if n < 3:
        print(0)
    else:
        j = bisect_right(lucky_numbers, n)
        print(sums[j - 1])
