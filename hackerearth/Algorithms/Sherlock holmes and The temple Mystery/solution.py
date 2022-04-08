testcases = int(input())
for _ in range(testcases):
    n = int(input())
    costs = list(map(int, input().strip().split()))
    print('NO' if sum(costs) % 2 else 'YES')
