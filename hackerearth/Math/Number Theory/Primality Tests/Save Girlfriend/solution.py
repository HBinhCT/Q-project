from math import ceil


def get_min_health(start, end):
    divisors = [0] * (end - start + 1)
    i = 1
    highest = 0
    while i * i <= end:
        j = max(i, int(ceil(start / i)) * i)
        while j <= end:
            divisors[j - start] += 1
            k = j // i
            if k * k > end:
                divisors[j - start] += 1
            highest = max(highest, divisors[j - start])
            j += i
        i += 1
    return divisors.count(highest) + 1


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(get_min_health(a, b))
