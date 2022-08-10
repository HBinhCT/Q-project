from sys import stdin
from collections import Counter


def make_mode(mode, arr):
    frequencies = Counter(arr)
    if len(frequencies) == 1:
        num = next(iter(frequencies))
        if mode == num:
            return 0
        else:
            return frequencies[num] // 2 + 1
    original_mode_fre = frequencies[mode]
    counter_frequencies = Counter(frequencies.values())
    list_counter = sorted(counter_frequencies.items(), reverse=True)
    list_counter.append((0, 0))
    if len(counter_frequencies) == 1:
        fre, count = list_counter[0]
        if fre == original_mode_fre:
            return 1 - (count == 1)
        else:
            return fre + 1 - fre // count
    mode_fre = frequencies[mode]
    total = 0
    for i in range(len(list_counter) - 1):
        fre, count = list_counter[i]
        next_fre, next_cnt = list_counter[i + 1]
        total += count
        if mode_fre == fre and total == 1:
            return 0
        next_mode_fre = (fre - next_fre) * total + mode_fre
        if next_mode_fre > next_fre:
            low = next_fre
            high = next_mode_fre
            while low < high:
                mid = (low + high) // 2
                quotient, remainder = divmod(next_mode_fre - mid, total)
                if mid > next_fre + quotient + (remainder > 0):
                    high = mid
                else:
                    low = mid + 1
            return high - original_mode_fre
        else:
            mode_fre = next_mode_fre


t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().strip().split())
    a = list(map(int, stdin.readline().strip().split()))
    print(make_mode(k, a))
