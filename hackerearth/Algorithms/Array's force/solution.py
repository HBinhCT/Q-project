"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

t = int(input())
for _ in range(t):
    arr = [0, 0]
    arr[0], arr[1], n, mod = map(int, input().split())
    mp = defaultdict(int)
    mp[arr[0]] += 1
    mp[arr[1]] += 1
    for i in range(n - 2):
        arr.append((arr[-1] + arr[-2]) % mod)
        if arr[-1] == arr[1] and arr[-2] == arr[0]:
            arr.pop()
            popping = arr.pop()
            mp[popping] -= 1
            q, r = divmod(n, len(arr))
            for j in mp:
                mp[j] = mp[j] * q
            for j in range(r):
                mp[arr[j]] += 1
            break
        else:
            mp[arr[-1]] += 1
    print(sum(mp[i] ** 2 for i in mp))
