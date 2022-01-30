"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
mod = 1000000007
for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input().strip()
    ways = [1]
    for i in range(len(s)):
        count = 0
        for j in range(i, -1, -1):
            if int(s[j:i + 1]) < k:
                count += ways[j]
                count %= mod
            else:
                break
        ways.append(count)
    print(ways[-1])
