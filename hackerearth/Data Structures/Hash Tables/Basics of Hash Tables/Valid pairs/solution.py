from collections import defaultdict


def solve(N, wealth):
    # Write your code here
    counter = defaultdict(int)
    count = 0
    for i in wealth:
        p = 1
        for _ in range(21):  # max is 3^20
            count += counter[p - i]
            p *= 3
        counter[i] += 1
    return count


N = int(input())
wealth = list(map(int, input().split()))

out_ = solve(N, wealth)
print(out_)
