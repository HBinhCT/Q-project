"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque, defaultdict


def find_time(sk, lk, arr):
    queue = deque([sk])
    counter = defaultdict(int)
    while queue:
        k = queue.popleft()
        for i in arr:
            x = (k * i) % 100000
            if x not in counter:
                counter[x] = counter[k] + 1
                if x == lk:
                    return counter[x]
                queue.append(x)
    return -1


samarpit_key, lock_key = map(int, input().strip().split())
n = int(input())
keys = list(map(int, input().strip().split()))
if samarpit_key == lock_key:
    print(0)
else:
    print(find_time(samarpit_key, lock_key, keys))
