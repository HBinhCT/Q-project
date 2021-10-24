"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import re
from collections import Counter
from itertools import chain

n = int(input())
hashtags = []
for _ in range(n):
    s = input().strip()
    hashtags.append(re.findall(r'#\w+', s))
hashtags = list(chain(*hashtags))
counter = Counter(hashtags)
for hashtag, count in sorted(counter.items(), key=lambda x: (-x[-1], x[0]))[:5]:
    print(hashtag)
