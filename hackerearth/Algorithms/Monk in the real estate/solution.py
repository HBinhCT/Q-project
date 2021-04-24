"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    e = int(input())
    cities = set()
    for _ in range(e):
        x, y = map(int, input().strip().split())
        cities.add(x)
        cities.add(y)
    print(len(cities))
