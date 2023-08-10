from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    elements = list(map(int, input().strip().split()))
    evens = []
    odds = []
    for i in elements:
        if i % 2:
            odds.append(i)
        else:
            evens.append(i)
    counter_evens = Counter(evens)
    counter_odds = Counter(odds)
    count = 0
    len_odds = len(odds)
    for i in range(len_odds):
        j = odds[i]
        count += len_odds - counter_odds[j] - i
        counter_odds[j] -= 1
    len_evens = len(evens)
    for i in range(len_evens):
        j = evens[i]
        count += len_evens - counter_evens[j] - i
        counter_evens[j] -= 1
    print(count)
