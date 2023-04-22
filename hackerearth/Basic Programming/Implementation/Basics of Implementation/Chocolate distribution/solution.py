def solution(chocolates, M, N):
    # Find the maximum number of chocolates that can be selected.
    prefixes = [0] * M
    max_sum = total = 0
    for i in chocolates:
        total += i
        remainder = total % M
        if remainder == 0:
            max_sum = max(max_sum, total)
        elif not prefixes[remainder]:
            prefixes[remainder] = total
        else:
            max_sum = max(max_sum, total - prefixes[remainder])
    return max_sum // M


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    chocolates = list(map(int, input().split()))

    out_ = solution(chocolates, M, N)
    print(out_)
