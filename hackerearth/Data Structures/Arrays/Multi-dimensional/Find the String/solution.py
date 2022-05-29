from collections import Counter

t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    matrix_counters = []
    for _ in range(n):
        matrix_counters.append(Counter(input().strip()))
    s = input()
    string_counters = [Counter(s[i::n]) for i in range(n)]
    for i in range(n):
        for key in string_counters[i]:
            if matrix_counters[i].get(key, 0) < string_counters[i][key]:
                print('No')
                break
        else:
            continue
        break
    else:
        print('Yes')
