"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

t = int(input())
for _ in range(t):
    l = input().strip()
    count_a = count_b = count_c = 0
    delta_patterns = defaultdict(int)
    delta_patterns[(0, 0)] = 1
    for c in l:
        if c == 'a':
            count_a += 1
        elif c == 'b':
            count_b += 1
        elif c == 'c':
            count_c += 1
        combine = (count_a - count_b, count_a - count_c)
        delta_patterns[combine] += 1
    result = 0
    for count in delta_patterns.values():
        if count > 1:
            result += (count - 1) * count // 2
    print(result)
