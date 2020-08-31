"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

s = input()
n = len(s)
if n == 0 or n == 1:
    print(n)
else:
    freq = defaultdict(int)
    max_char = len(set(s))
    min_len = n + 1
    start = 0
    ans = n + 1
    for i in range(n):
        freq[s[i]] += 1
        if len(freq) == max_char:
            while start < i and freq[s[start]] > 1:
                freq[s[start]] -= 1
                start += 1
            curr_len = i - start + 1
            min_len = min(min_len, curr_len)
    print(min_len)
