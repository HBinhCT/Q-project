"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, col = map(int, input().strip().split())
list_a = []
list_b = []
for _ in range(n):
    a, b = map(float, input().strip().split())
    list_a.append(a)
    list_b.append(b)
k = float(input())
r_min = -min(list_b) + 10e-6
r_max = (n + 1) * 1000
r = (r_min + r_max) / 2
sum_all_ratios = lambda list_x, list_y, z: sum(x / (y + z) for x, y in zip(list_x, list_y))
sum_ratios = sum_all_ratios(list_a, list_b, r)
while abs(k - sum_ratios) > 10e-6:
    if sum_ratios > k:
        r_min = r
    else:
        r_max = r
    r = (r_min + r_max) / 2
    sum_ratios = sum_all_ratios(list_a, list_b, r)
print(f'{r:.8f}')
