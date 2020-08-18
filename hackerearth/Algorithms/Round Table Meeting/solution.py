"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
for _ in range(q):
    x, y = map(int, input().strip().split())
    if x == y:
        print(0)
    else:
        ans = n - 1
        matched_idx = init_idx = None
        for i in range(n):
            if a[i] == x or a[i] == y:
                if matched_idx is None:
                    matched_idx = init_idx = i
                else:
                    if a[i] != a[matched_idx]:
                        ans = min(ans, (i - matched_idx) // 2)
                    matched_idx = i
        if a[init_idx] != a[matched_idx]:
            ans = min(ans, (init_idx - (matched_idx - n)) // 2)
        print(ans)
