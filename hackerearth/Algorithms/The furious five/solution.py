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
    power_five = 5
    sum_exps_five = 1
    while sum_exps_five <= n:
        power_five *= 5
        sum_exps_five = sum_exps_five * 5 + 1
    remainder = n
    res = 0
    while remainder > 0:
        power_five //= 5
        sum_exps_five = (sum_exps_five - 1) // 5
        q, remainder = divmod(remainder, sum_exps_five)
        res += q * power_five
    print(res)
