from itertools import combinations

s, k = input().rstrip().split()
print(*[''.join(j) for i in range(1, int(k) + 1) for j in combinations(sorted(s), i)], sep='\n')
