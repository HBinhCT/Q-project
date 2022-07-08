from collections import defaultdict

m, n = map(int, input().strip().split())
ages = map(int, input().strip().split())
counter = defaultdict(int)
awarded = -1
counter[awarded] = -1
for age in ages:
    counter[age] += 1
    if counter[age] > counter[awarded] or counter[age] == counter[awarded] and age > awarded:
        awarded = age
    print(awarded, counter[awarded])
