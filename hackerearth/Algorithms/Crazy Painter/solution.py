"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().strip().split()))
    total_points = n * 12
    freq, additional = divmod(total_points, 26)
    ans = 0
    if freq > 0:
        ans += sum(c) * freq + freq * (freq - 1) // 2 * 26
        ans += sum(c[:additional]) + freq * additional
    else:
        ans += sum(c[:additional])
    print(ans)
