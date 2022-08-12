n = int(input().strip())
a = list(map(int, input().strip().split()))
increasing = 1
decreasing = 0
for i in range(1, n):
    new_increasing, new_decreasing = increasing, decreasing
    if a[i - 1] >= a[i]:
        decreasing = new_increasing + 1
    if a[i - 1] <= a[i]:
        increasing = new_decreasing + 1
print(max(increasing, decreasing))
