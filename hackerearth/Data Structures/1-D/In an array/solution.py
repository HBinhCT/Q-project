from collections import defaultdict

n, k, x, y = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
if k == 1:
    print(n * (n - 1) // 2)
else:
    counter = defaultdict(int)
    for i in a:
        counter[i % k] += 1
    count = 0
    checked = set()
    for i in range(k):
        if i not in checked:
            checked.add(i)
            j = (0 if i <= x else k) + x - i
            checked.add(j)
            if i * j % k == y:
                if i != j:
                    count += counter[i] * counter[j]
                else:
                    count += counter[i] * (counter[i] - 1) // 2
    print(count)
