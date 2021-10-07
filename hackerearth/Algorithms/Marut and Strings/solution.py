"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
try:
    t = int(input())
    assert 1 <= t <= 10
    for _ in range(t):
        try:
            s = input()
            assert 1 <= len(s) <= 100
            assert any(c.isalpha() for c in s)
            low = up = 0
            for c in s:
                if c.isalpha():
                    if 'A' <= c <= 'Z':
                        up += 1
                    else:
                        low += 1
            print(min(low, up))
        except:
            print('Invalid Input')
except:
    print('Invalid Test')
