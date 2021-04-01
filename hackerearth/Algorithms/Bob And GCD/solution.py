"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    k, n = map(int, input().strip().split())
    a = map(int, input().strip().split())
    mid = k / 2
    step = 0
    for i in a:
        mod = i % k
        if i < k:
            step += k - i
        elif mod > mid:
            step += k - mod
        else:
            step += mod
    print(step)
