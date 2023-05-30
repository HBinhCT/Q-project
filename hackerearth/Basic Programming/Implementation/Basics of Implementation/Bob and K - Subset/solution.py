n, k = map(int, input().strip().split())
a = map(int, input().strip().split())
subset1 = subset2 = set(a)
for _ in range(2, k + 1):
    subset2 = set(i | j for i in subset2 for j in subset2 if i | j not in subset1)
    subset1.update(subset2)
print(len(subset1))
