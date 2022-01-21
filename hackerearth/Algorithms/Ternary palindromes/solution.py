"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if n == 1 or n == 2 and s[0] != s[1]:
        print(2)
    else:
        z = s.count('0')
        o = s.count('1')
        t = s.count('2')
        srt = sorted([z, o, t])
        if srt[-1] - srt[0] > 1 or 0 in srt:
            print(0)
        elif len(set(srt)) == 1:
            print(6)
        else:
            print(2)
