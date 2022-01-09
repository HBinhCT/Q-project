"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input().strip()
arr = list(map(int, list(s)))
n = len(arr)
count = 0
for i in arr:
    count += i % 2 == 0
counter = [0] * n
counter[0] = count
for i in range(n - 1):
    counter[i + 1] = counter[i] - (1 - arr[i] % 2)
print(' '.join(map(str, counter)))
