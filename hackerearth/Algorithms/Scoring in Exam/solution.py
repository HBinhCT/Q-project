"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, q = map(int, input().strip().split())
t = map(int, input().strip().split())
s = map(int, input().strip().split())
data = sorted(zip(s, t), reverse=True)
time_required = [0] * n
time_required[0] = data[0][1]
for i in range(1, n):
    time_required[i] = time_required[i - 1] + data[i][1]
for _ in range(q):
    k = int(input())
    print(time_required[k - 1])
