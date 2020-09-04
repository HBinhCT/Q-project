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
    coins = list(map(int, input().strip().split()))
    low = 0
    high = c = max(coins + [n])
    while low <= high:
        mid = (low + high) // 2
        stack_coins = max(coins[0] - mid, 1)
        possible = True
        for i in range(1, n):
            if coins[i] + mid <= stack_coins:
                possible = False
                break
            stack_coins = max(coins[i] - mid, stack_coins + 1)
        if possible:
            high = mid - 1
            c = min(c, mid)
        else:
            low = mid + 1
    print(c)
