def solve(N, workload):
    # Write your code here
    max_days = 0
    days = []
    for i in range(N):
        if workload[i] > 6:
            max_days += 1
        else:
            if max_days > 0:
                days.append(max_days)
            max_days = 0
    return max(days)


N = int(input())
workload = list(map(int, input().split()))

out_ = solve(N, workload)
print(out_)
