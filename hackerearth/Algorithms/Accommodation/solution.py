"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
m, n = map(int, input().strip().split())
c = list(map(int, input().strip().split()))
accommodation = [0] * (n + 1)
accommodation[0] = 1
for i in c:
    for j in range(i, n + 1):
        accommodation[j] += accommodation[j - i]
        accommodation[j] %= 1000000007
print(accommodation[n])
