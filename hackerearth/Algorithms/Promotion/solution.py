"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math

n, m = map(int, input().strip().split())
boxes = sorted(map(int, input().strip().split()))  # weight of each box
trucks = sorted(map(int, input().strip().split()))  # maximum capacity of each truck
rounds = math.ceil(n / m)
i = n - 1 - rounds
j = m - 2
while i >= 0:
    if trucks[j] >= boxes[i]:
        i -= rounds
        j -= 1
    else:
        rounds += 1
        i -= m - j - 1
print(rounds * 2 - 1)
