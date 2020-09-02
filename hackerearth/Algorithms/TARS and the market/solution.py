"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, sp = map(int, input().strip().split())
b = list(map(int, input().strip().split()))
k = n
while k >= 0:
    costs = sorted(b[i] + ((i + 1) * k) for i in range(n))
    t = sum(costs[0:k])
    if t <= sp:
        print(k, t)
        break
    else:
        k -= 1
