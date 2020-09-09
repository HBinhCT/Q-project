"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
a = list(map(int, input().strip().split()))
mid = (n + 1) // 2
first_list = a[:mid]
second_list = a[mid:]
counts = defaultdict(int)
temp = [0]
for i in second_list:
    j = len(temp)
    while j > 0:
        j -= 1
        temp.append(i ^ temp[j])
for i in temp:
    counts[i] += 1
ans = counts[0]
temp = [0]
for i in first_list:
    j = len(temp)
    while j > 0:
        j -= 1
        val = i ^ temp[j]
        temp.append(val)
        ans += counts[val]
print(ans - 1)
