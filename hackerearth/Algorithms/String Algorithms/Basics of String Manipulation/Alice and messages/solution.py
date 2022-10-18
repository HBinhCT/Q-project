from string import ascii_lowercase

n = int(input())
strings = input().strip()
for i in range(26):
    strings = strings.replace(ascii_lowercase[i], ascii_lowercase[-i - 1])
print(len(set(strings.split())))
