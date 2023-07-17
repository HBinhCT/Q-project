from itertools import accumulate

n, q = map(int, input().strip().split())
a = list(accumulate(map(lambda x: int(x).bit_length(), input().strip().split()), initial=0))
for _ in range(q):
    l, r = map(int, input().strip().split())
    print('Mishki' if a[r] - a[l - 1] & 1 else 'Hacker')
