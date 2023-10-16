n = int(input())
arr = list(map(int, input().strip().split()))
for i in arr:
    x = bin(i)[2:]
    c = x.count("1")
    x = "1" * c + "0" * (len(x) - c)
    print(int(x, 2), end=" ")
