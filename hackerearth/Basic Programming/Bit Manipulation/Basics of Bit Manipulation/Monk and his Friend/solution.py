t = int(input())
for _ in range(t):
    p, m = map(int, input().strip().split())
    print(str(bin(m ^ p)).count("1"))
