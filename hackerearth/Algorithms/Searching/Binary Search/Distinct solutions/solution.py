t = int(input())
for _ in range(t):
    n, t1, t2 = map(int, input().strip().split())
    low = 0
    high = 10 ** 18
    while low < high:
        mid = (low + high) >> 1
        if mid // t1 + mid // t2 >= n:
            high = mid
        else:
            low = mid + 1
    if not high % t1 and high % t2:
        print(1 + high // t1 + high // t2, (high // t2 + 1) * t2)
    elif high % t1 and not high % t2:
        print(1 + high // t1 + high // t2, (high // t1 + 1) * t1)
    else:
        print(high // t1 + high // t2, high)
