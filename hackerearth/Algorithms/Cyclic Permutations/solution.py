"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())


def kmp(text, pattern, n):
    res = 0
    pattern = list(pattern)
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos - shift]:
            shift += shifts[pos - shift]
        shifts[pos + 1] = shift
    start_pos = 0
    match_len = 0
    for c in text:
        while match_len == len(pattern) or match_len >= 0 and pattern[match_len] != c:
            start_pos += shifts[match_len]
            match_len -= shifts[match_len]
        match_len += 1
        if match_len == len(pattern) and start_pos < n:
            res += 1
    return res


for _ in range(t):
    a = input()
    b = input()
    b += b
    print(kmp(b, a, len(a)))
