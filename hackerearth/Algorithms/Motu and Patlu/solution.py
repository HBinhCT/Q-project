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
    a = list(map(int, input().strip().split()))
    x = 1
    y = n - 1
    first_ice = a[0] / 2
    second_ice = 0
    while x <= y:
        mid = (y - x) // 2 + x
        first_half = sum(a[x:mid]) / 2 + first_ice
        second_half = sum(a[mid + 1:y + 1]) + second_ice
        if first_half == second_half:
            x = mid + 1
            first_ice = first_half + a[mid] / 2
            first_half = first_ice
            if second_ice != 0:
                second_half = second_ice
                break
        elif first_half < second_half:
            first_ice = first_half + a[mid] / 2
            first_half = first_ice
            x = mid + 1
        else:
            second_ice = second_half + a[mid]
            second_half = second_ice
            y = mid - 1
    motu_eat = x
    patlu_eat = n - motu_eat
    print(motu_eat, patlu_eat)
    if motu_eat > patlu_eat:
        print('Motu')
    elif motu_eat < patlu_eat:
        print('Patlu')
    else:
        print('Tie')
