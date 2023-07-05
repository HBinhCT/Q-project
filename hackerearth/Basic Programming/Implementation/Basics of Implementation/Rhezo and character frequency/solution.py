s = input().strip()
c = input().strip()
p = int(input())
max_freq = pos = count_subs = count_c = 0
for i in range(len(s) - p + 1):
    j = i + p
    freq = s[i:j].count(c)
    if freq > max_freq:
        max_freq = freq
        count_subs = 1
        if c == s[i]:
            if c == s[j - 1]:
                count_c = 1
            else:
                count_c = 0
                pos = j - 1
        else:
            count_c = 0
            pos = j
    elif freq == max_freq:
        count_subs += 1
        if c == s[i]:
            if c == s[j - 1]:
                count_c += 1
        else:
            pos = j
print(pos if count_subs != count_c else -1)
