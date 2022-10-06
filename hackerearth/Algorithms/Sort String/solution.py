from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    zeros = s.count('0')
    if zeros == 0 or zeros == n:
        print(0)
        continue
    left_ones = 0
    right_ones = n - zeros
    min_flips = min(right_ones, zeros)
    for i in range(n):
        if s[i] == '1':
            flips = left_ones + n - i - right_ones
            min_flips = min(min_flips, flips)
            left_ones += 1
            right_ones -= 1
    print((min_flips + 1) // 2)
