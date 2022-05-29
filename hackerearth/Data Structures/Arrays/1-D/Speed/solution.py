t = int(input())
for _ in range(t):
    n = int(input())
    speeds = list(map(int, input().strip().split()))
    max_speed = speeds[0]
    count = 0
    for i in speeds:
        if max_speed >= i:
            count += 1
            max_speed = i
    print(count)
