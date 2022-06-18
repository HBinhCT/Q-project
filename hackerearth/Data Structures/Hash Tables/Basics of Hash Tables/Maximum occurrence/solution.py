from collections import Counter

s = input().strip()
print(*Counter(sorted(s)).most_common(1)[0])
