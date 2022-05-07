n = int(input())
a = list(input().strip().split())
max_len = 0
for i in map(str, range(10)):
    count = 0
    for j in a:
        if i in j:
            count += 1
    max_len = max(max_len, count)
print(max_len)
