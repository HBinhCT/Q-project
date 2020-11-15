"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

n = int(sys.stdin.readline())
max_point = 0
restaurant = ''
for _ in range(n):
    name, point = sys.stdin.readline().strip().split()
    if int(point) > max_point:
        max_point = int(point)
        restaurant = name
    elif max_point == int(point):
        restaurant = min(restaurant, name)
print(restaurant)
