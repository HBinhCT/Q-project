n = int(input())
k = int(input())
a = list(map(int, input().strip().split()))
if k == 0:
    print(1)
else:
    maximum = a[0]
    length = 1
    start = total = prev_length = 0
    for i in range(1, n):
        length = i - start + 1
        if maximum < a[i]:
            total = 0
            maximum = a[i]
            j = start
            while j <= i:
                total += maximum - a[j]
                j += 1
        else:
            total += maximum - a[i]
        if total > k:
            if a[start] == maximum:
                total = 0
                start += 1
                maximum = max(a[start:i])
                j = start
                while j <= i:
                    total += maximum - a[j]
                    j += 1
            else:
                total -= maximum - a[start]
                length = i - start
                start += 1
        elif total == k:
            prev_length = max(length, prev_length)
            total -= maximum - a[start]
            start += 1
    print(max(length, prev_length))
