"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict
from itertools import accumulate


def type_one_handler(arr, queries):
    temp = [0] * (n + 1)
    for i, start, end in queries:
        temp[start - 1] += i
        temp[end] -= i
    temp = accumulate(temp)
    return [sum(i) for i in zip(arr, temp)]


n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
queries = []
for _ in range(q):
    queries.append(tuple(map(int, input().strip().split())))
first = defaultdict(list)
second = defaultdict(list)
for type_query, left, right, x in queries:
    if x < 0:
        first[type_query - 1].append((x, left, right))
    else:
        second[type_query - 1].append((x, left, right))
first[1] += second[1]
second[1] = []
first[1].sort()
a = type_one_handler(a, first[0])
for x, left, right in first[1]:
    a[left - 1:right] = [x] * (right - left + 1)
a = type_one_handler(a, second[0])
print(*a)
