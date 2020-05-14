from itertools import combinations_with_replacement

s, k = input().rstrip().split()
print(*[''.join(p) for p in combinations_with_replacement(sorted(s), int(k))], sep='\n')
