from itertools import accumulate

n = int(input())
a = list(map(int, input().strip().split()))
sums = list(accumulate(a))
vals = []
for i in range(n):
    j = int((2 * (n - i)) ** .5)
    while j > 0 and i + j * (j + 1) // 2 - 1 >= n:
        j -= 1
    val = sums[i + j * (j + 1) // 2 - 1]
    if i > 0:
        val -= sums[i - 1]
    vals.append(val)
print(max(vals))
