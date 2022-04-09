from functools import lru_cache


@lru_cache(maxsize=None)
def Min_and_Max(Arr):
    # // returns an array where the first element is the minimum sum and the
    # second is the maximum sum .
    if len(Arr) == 2:
        power = Arr[0] ^ Arr[1]
        return power, power
    minimum = float('inf')
    maximum = 0
    for i in range(1, len(Arr)):
        val = Arr[0] ^ Arr[i]
        res = Min_and_Max(Arr[1:i] + Arr[i + 1:])
        minimum = min(res[0] + val, minimum)
        maximum = max(res[1] + val, maximum)
    return minimum, maximum


n = int(input())
Arr = []
for _ in range(n):
    Arr.append(int(input()))

out_ = Min_and_Max(tuple(Arr))
print(' '.join(map(str, out_)))
