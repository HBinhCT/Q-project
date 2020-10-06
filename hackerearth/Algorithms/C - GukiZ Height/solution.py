"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, h = map(int, input().strip().split())
a = list(map(int, input().strip().split()))


def find(x, goal, accumulated, tot):
    ht = goal - (x * (x + 1)) // 2
    st = tot * ((x - 1) // n) + accumulated[(x - 1) % n]
    return ht <= st


def search(start, end, goal, accumulated, tot):
    if start > end:
        for i in range(start - n, start + 1):
            if find(i, goal, accumulated, tot):
                print(i)
                break
        return
    mid = (start + end) // 2
    if find(mid, goal, accumulated, tot):
        search(start, mid - 1, goal, accumulated, tot)
    else:
        search(mid + 1, end, goal, accumulated, tot)


counter = [0] * n
counter[0] = a[0]
total = sum(a)
for i in range(1, n):
    counter[i] = counter[i - 1] + a[i]
    if find(i, h, counter, total):
        print(i)
        break
else:
    search(1, int(2e9), h, counter, total)
