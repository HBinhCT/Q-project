from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    total = count = 0
    counter = Counter(a)
    for i in set(a):
        if not counter[i] % i:
            x = counter[i] // i
            total += i * x
            count += x
    print('Invalid Data' if n != total else count)
