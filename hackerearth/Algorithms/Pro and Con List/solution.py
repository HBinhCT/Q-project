"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    top_1_girl = 0  # sum of favour and anger of one girl
    top_2_girl = 0  # sum of another girl
    all_anger_girls = 0  # anger of all girls
    n = int(input())
    for __ in range(n):
        favour, anger = map(int, input().strip().split())
        sum_favour_anger = favour + anger
        if sum_favour_anger > top_1_girl:
            top_1_girl, top_2_girl = sum_favour_anger, top_1_girl
        elif sum_favour_anger > top_2_girl:
            top_2_girl = sum_favour_anger
        all_anger_girls += anger
    print(top_1_girl + top_2_girl - all_anger_girls)
