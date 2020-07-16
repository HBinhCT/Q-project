"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = map(int, input().strip().split())
subset = []
neg_nums = []
for i in a:
    if i >= 0:
        subset.append(i)
    else:
        neg_nums.append(i)
if subset:
    print(sum(subset), len(subset))
    del neg_nums
else:
    print(max(neg_nums), 1)
