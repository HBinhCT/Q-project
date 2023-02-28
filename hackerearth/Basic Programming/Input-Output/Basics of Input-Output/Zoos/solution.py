from collections import Counter

word = input().strip()
counter = Counter(word)
print('Yes' if counter['z'] * 2 == counter['o'] else 'No')
