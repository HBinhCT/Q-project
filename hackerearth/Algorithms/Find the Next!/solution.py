"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, q = map(int, input().split())
a = list(map(int, input().strip().split()))
val = [1] * n
d = dict(zip(a, val))
query = []
res = {}
for _ in range(q):
    x = int(input())
    query.append(x)
    res[x] = 0
query_copy = query.copy()
query_copy.sort()
prev = 0
for x in query_copy:
    if prev > x:
        res[x] = prev
    else:
        i = x + 1
        while i in d:
            i += 1
        res[x] = i
        prev = i
for i in query:
    print(res[i])
