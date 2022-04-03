m = int(input())
p = int(input())
weights = list(map(int, input().strip().split()))
high = sum(weights)
low = 0
while high >= low:
    mid = (high + low) // 2
    total = count = 0
    for w in weights:
        total += w
        if total > mid:
            count += 1
            total = w
            if total > mid:
                count = -1
                break
    if count == -1 or count >= m:
        low = mid + 1
    else:
        high = mid - 1
print(low)
