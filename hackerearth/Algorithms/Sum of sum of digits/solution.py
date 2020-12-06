"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from itertools import accumulate

n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = [i % 9 if i % 9 != 0 else 9 for i in a]
b.sort()
left_list = list(accumulate(b))
right_list = sorted(accumulate(reversed(b)), reverse=True)
for _ in range(q):
    query_type, k = map(int, input().strip().split())
    if query_type == 1:
        print(right_list[n - k])
    elif query_type == 2:
        print(left_list[k - 1])
