from sys import stdin
from collections import Counter


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().strip().split()))
        counter = Counter(a)
        freq = [0, counter[1]]
        for i in range(2, 100001):
            freq.append(freq[-1] + counter[i])
        ans = 0
        for i in range(1, 100001):
            if freq[i] - freq[i - 1]:
                bottom = i // 2 - (i % 2 == 0)
                top = bottom + i
                for j in range(1, 100001):
                    if bottom > 100000:
                        break
                    ans += j * (freq[i] - freq[i - 1]) * (freq[top if top < 100001 else 100000] - freq[bottom])
                    top += i
                    bottom += i
        print(ans)


solve()
