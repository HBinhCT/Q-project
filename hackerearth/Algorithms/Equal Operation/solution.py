from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().strip().split()))
    minimum = a[0]
    has_remainder = True
    operations = 0
    while has_remainder:
        operations = 0
        has_remainder = False
        for i in a:
            operations += i // minimum - 1
            remainder = i % minimum
            if remainder:
                minimum = remainder
                has_remainder = True
                break
    print(operations)
