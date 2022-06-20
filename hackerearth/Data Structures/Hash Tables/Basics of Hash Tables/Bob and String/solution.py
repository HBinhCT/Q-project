from collections import Counter

t = int(input())
for _ in range(t):
    string_s = input().strip()
    string_t = input().strip()
    counter_s = Counter(string_s)
    counter_t = Counter(string_t)
    count = 0
    for i in counter_t:
        if i in counter_s:
            count += abs(counter_s[i] - counter_t[i])
        else:
            count += counter_t[i]
    for i in counter_s:
        if i not in counter_t:
            count += counter_s[i]
    print(count)
