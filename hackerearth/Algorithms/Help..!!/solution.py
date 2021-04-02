"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from operator import itemgetter

n = int(input())
arr = []
for i in range(n):
    s, f = map(int, input().strip().split())
    arr.append([s, f])
d, p = map(int, input().strip().split())
for i in range(n):
    arr[i][0] = d - arr[i][0]
arr.sort(key=itemgetter(0))
i = j = stops = 0
while d > p and i < n:
    mx_acquire = 0
    curr_stop = 0
    if arr[i][0] > p:
        break
    while i < n and arr[i][0] <= p:
        if arr[i][1] > mx_acquire:
            mx_acquire = arr[i][1]
            curr_stop = arr[i][0]
            j = i
        i += 1
    stops += 1
    i = j + 1
    p += mx_acquire
if d > p:
    print(-1)
else:
    print(stops)
