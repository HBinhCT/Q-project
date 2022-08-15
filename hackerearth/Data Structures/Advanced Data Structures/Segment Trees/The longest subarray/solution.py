from collections import defaultdict
from sys import stdin

max_range = 61
max_2k = 2 ** (max_range + 1) - 1
list_2k = [2 ** i for i in range(max_range)]
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().strip().split()))
    lengths = [0] * max_range
    for i in range(max_range):
        length = 0
        bitwise_2k = max_2k
        val_2k = list_2k[i]
        for j in a:
            if j & val_2k:
                bitwise_2k &= j
                length += 1
                if bitwise_2k == val_2k and length > lengths[i]:
                    lengths[i] = length
            else:
                length = 0
                bitwise_2k = max_2k
    longest_lengths = defaultdict(list)
    for i in range(max_range):
        for j in range(max_range):
            longest_lengths[i].append(max(lengths[i:j + 1]) if j >= i else 0)
    q = int(stdin.readline())
    for _ in range(q):
        l, r = map(int, stdin.readline().strip().split())
        print(longest_lengths[l][r])
