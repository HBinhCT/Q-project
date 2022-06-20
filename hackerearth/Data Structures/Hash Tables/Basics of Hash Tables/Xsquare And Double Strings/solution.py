from collections import Counter

t = int(input())
for _ in range(t):
    s = input().strip()
    print('Yes' if Counter(s).most_common(1)[0][-1] > 1 else 'No')
