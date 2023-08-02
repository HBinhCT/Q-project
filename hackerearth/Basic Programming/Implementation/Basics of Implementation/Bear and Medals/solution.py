t = int(input())
for _ in range(t):
    n = int(input())
    result = gold = silver = bronze = 0
    for _ in range(n):
        g, s, b = map(int, input().strip().split())
        gold += g
        silver += s
        bronze += b
        result = max(result, g + s + b, gold, silver, bronze)
    print(result)
