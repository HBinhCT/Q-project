t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    inverse_arr = [arr.index(i) + 1 for i in range(1, n + 1)]
    print("inverse" if arr == inverse_arr else "not inverse")
