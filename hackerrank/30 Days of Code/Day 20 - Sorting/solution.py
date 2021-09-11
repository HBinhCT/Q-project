#!/bin/python3

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
number_of_swaps = 0
while True:
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            a[i + 1], a[i] = a[i], a[i + 1]
            number_of_swaps += 1
            break
    else:
        break
print(f'Array is sorted in {number_of_swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')
