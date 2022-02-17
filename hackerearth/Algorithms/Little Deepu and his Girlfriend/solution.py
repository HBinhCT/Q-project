"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
players = {
    1: 'Kate',
    2: 'Little Deepu',
}
for _ in range(t):
    m, n = map(int, input().strip().split())
    s = list(map(int, input().strip().split()))
    res = [False] * m
    for i in s:
        res[i - 1] = True
    for i in range(m):
        if not res[i]:
            for j in s:
                if i + j < m:
                    res[i + j] = True
    print(players[res[-1] + 1])
