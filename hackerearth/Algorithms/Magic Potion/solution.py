"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
count_arr = 0
magic_potion = n
total = 0
i = 0
j = -1
lyralei = 0  # Compass of the Rising Gale — Windranger Arcana
while i < n:
    total += a[i]
    while total > k:
        j += 1
        total -= a[j]
        if lyralei != 0:
            lyralei = 0
    while j < n - 1 and a[j + 1] == 0:
        j += 1
        lyralei += 1
    if total == k:
        count_arr += lyralei + 1
        magic_potion = min(magic_potion, n - (i - j) - lyralei)
    i += 1
print(count_arr, magic_potion)
