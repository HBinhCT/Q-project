s = input().strip()
longest = 0
count = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1
    else:
        longest = max(longest, count)
        count = 1
print(max(longest, count))
