"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, k = map(int, input().strip().split())
marks = sorted(map(int, input().strip().split()))
x = 0
prev_is_plagiarism = 0
for i in range(1, len(marks)):
    if marks[i] - marks[i - 1] <= k:
        if prev_is_plagiarism:
            x += 1
        else:
            x += 2
        prev_is_plagiarism = 1
    else:
        prev_is_plagiarism = 0
print(f'{x} students need to worry!')
print(f'{n - x} students should relax!')
