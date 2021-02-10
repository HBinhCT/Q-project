"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
hunger_values = sorted(map(int, input().strip().split()))
ans = 0
for i in range(n - 2):
    ans = max(ans, hunger_values[i + 2] - hunger_values[i])
print(ans)
