from collections import defaultdict
from operator import itemgetter
from string import ascii_lowercase
from sys import stdin
from itertools import chain

t = int(stdin.readline())
for _ in range(t):
    s = stdin.readline().strip()
    counter = defaultdict(list)
    for c in reversed(ascii_lowercase):
        times = s.count(c)
        counter[times].append(c)
        if len(counter[times]) > 1:
            counter[times].sort(reverse=True)
    ans = [item[-1] for item in sorted(counter.items(), key=itemgetter(0))]
    print(' '.join(chain.from_iterable(ans)))
