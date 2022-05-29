from itertools import accumulate

n = int(input())
a = list(map(int, input().strip().split()))
sums = list(accumulate(a, initial=0))
squares = set()
x = 1
while 1:
    y = x * x
    squares.add(y)
    if y > sums[-1]:
        break
    x += 1
count = 0
for i in range(1, n + 1):
    for j in range(i):
        count += (sums[i] - sums[j]) in squares
print(count)
