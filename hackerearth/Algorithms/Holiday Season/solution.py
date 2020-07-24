"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
s = input()

# ----- Basic Method -----
# counter = [0] * 26
# ans = 0
# counter[ord(s[0]) - 97] += 1  # 97 is ord('a')
# for i in range(1, n):
#     count = 0
#     for j in range(i + 1, n):
#         if s[i] == s[j]:
#             ans += count
#         count += counter[ord(s[j]) - 97]
#     counter[ord(s[i]) - 97] += 1
# print(ans)

# ----- ಠ_ಠ I have no idea what I'm doing (╯°□°)╯︵ ┻━┻ -----
counter = defaultdict(list)
for i in range(n):
    counter[s[i]].append(i)
ans = 0
chars = list(counter.keys())
size = len(chars)
for i in range(size - 1):
    for j in range(i + 1, size):
        a = counter[chars[i]]
        b = counter[chars[j]]
        size_a = len(a)
        size_b = len(b)
        temp = sorted(a + b)
        count_a = [size_b - temp.index(a[x]) + x for x in range(size_a)]
        count_b = [size_a - temp.index(b[x]) + x for x in range(size_b)]
        for x in range(len(count_a) - 1):
            for y in range(x + 1, len(count_a)):
                ans += count_a[y] * (count_a[x] - count_a[y])
        for x in range(len(count_b) - 1):
            for y in range(x + 1, len(count_b)):
                ans += count_b[y] * (count_b[x] - count_b[y])
for k, v in counter.items():
    if len(v) >= 4:
        size_v = len(v)
        ans += (size_v * (size_v - 1) * (size_v - 2) * (size_v - 3)) // 24  # 24 = 4 * 3 * 2 * 1
print(ans)
