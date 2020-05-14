from itertools import permutations

s, k = input().rstrip().split()
print(*[''.join(i) for i in permutations(sorted(s), int(k))], sep='\n')
