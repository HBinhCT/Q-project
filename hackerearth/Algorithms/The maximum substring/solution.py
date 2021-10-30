"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import Counter

s = input()
counter = Counter(s)
max_count = max(counter.values())
substrings = []
for i in counter:
    if counter[i] == max_count:
        substrings.append(i)
res = ''.join(substrings)
print(res[0:max_count + 1])
