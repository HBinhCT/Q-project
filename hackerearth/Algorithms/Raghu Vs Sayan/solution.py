"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    kCals = list(map(int, input().split()))
    if a == b:
        print('Tie')
    else:
        raghu_count = sayan_count = raghu_done = sayan_done = 0
        kCals.sort()
        for kCal in kCals:
            if raghu_done != 1:
                if a - kCal >= 0:
                    a -= kCal
                    raghu_count += 1
                else:
                    raghu_done = 1
            if sayan_done != 1:
                if b - kCal >= 0:
                    b -= kCal
                    sayan_count += 1
                else:
                    sayan_done = 1
            if raghu_done == sayan_done == 1:
                break
        if raghu_count > sayan_count:
            print('Raghu Won')
        elif sayan_count > raghu_count:
            print('Sayan Won')
        else:
            print('Tie')
