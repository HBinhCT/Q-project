"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    distance = abs(b - a)
    jumps = distance // 5
    distance -= jumps * 5
    more = distance // 2
    if more:
        jumps += more
    if distance % 2:
        jumps += 1
    print(jumps)
