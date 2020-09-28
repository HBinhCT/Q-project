"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = list(map(int, input().strip().split()))
k = int(input())


def rasengan(arr, target, i, chakra):
    if chakra >= target:
        return 2 ** (len(arr) - i + 1)
    else:
        if i > len(arr):
            return 0
        else:
            return rasengan(arr, target, i + 1, chakra + arr[i - 1]) + rasengan(arr, target, i + 1, chakra)


print(rasengan(a, k, 1, 0))
