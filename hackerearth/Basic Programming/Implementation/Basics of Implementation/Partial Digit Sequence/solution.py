from string import digits

counter = {i: 0 for i in digits}
n = input()
a = map(set, input().strip().split())
for i in a:
    cnt = 0
    for d in i:
        cnt = max(cnt, counter[d])
    cnt += 1
    for d in i:
        counter[d] = cnt
print(max(counter.values()))
