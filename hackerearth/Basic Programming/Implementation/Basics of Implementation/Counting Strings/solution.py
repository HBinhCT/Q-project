t = int(input())
for _ in range(t):
    m = input().strip()
    n = len(m)
    s = m.replace("a", " ").replace("z", " ").split()
    count = 0
    for i in s:
        x = len(i)
        count += x * (x + 1) // 2
    print(n * (n + 1) // 2 - count)
