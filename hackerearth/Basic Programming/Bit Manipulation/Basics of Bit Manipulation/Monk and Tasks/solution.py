t = int(input())
for _ in range(t):
    n = int(input())
    array = sorted(map(int, input().strip().split()), key=lambda x: bin(x).count("1"))
    print(" ".join(map(str, array)))
