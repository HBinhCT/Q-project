n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
sub = set()
counter = [0] * n
for i in range(n - 1, -1, -1):
    sub.add(a[i])
    counter[i] = len(sub)
for _ in range(q):
    j = int(input())
    j -= 1
    print(counter[j])
