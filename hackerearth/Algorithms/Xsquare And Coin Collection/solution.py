"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    coins = list(map(int, input().strip().split()))
    mx = curr = 0
    for i in coins:
        if i <= k:
            curr += i
            mx = max(mx, curr)
        else:
            curr = 0
    print(mx)
