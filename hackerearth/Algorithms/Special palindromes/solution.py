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
    s = input()
    tracks = [0, 0]
    counts = [0, 1]
    pos = 0
    for i in range(1, n):
        while pos > 0 and s[i] != s[pos]:
            pos = tracks[pos]
        if s[pos] == s[i]:
            pos += 1
        tracks.append(pos)
        counts.append(counts[pos] + 1)
    print(sum(counts))
