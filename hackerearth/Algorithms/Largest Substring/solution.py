"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
s = input()
max_len = total = 0
prev_sum = {}
for i in range(n):
    if s[i] == '0':
        total += 1
    else:
        total -= 1
    if total > 0:
        max_len = i + 1
    elif (total - 1) in prev_sum:
        max_len = max(max_len, i - prev_sum[total - 1])
    if total not in prev_sum:
        prev_sum[total] = i
print(max_len)
