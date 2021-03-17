"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = sorted(map(int, input().strip().split()))
q = int(input())


def binary_search(lines, item):
    low = 0
    high = len(lines) - 1
    while low <= high:
        mid = (low + high) // 2
        if lines[mid] == item:
            return mid
        if lines[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return low


for _ in range(q):
    x, y = map(int, input().strip().split())
    print(binary_search(a, x + y))
