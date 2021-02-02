"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from sys import stdin
from collections import deque


def get_shifted_idx(pending, top_elem_idx, max_shifted_idx):
    for digit in range(10):
        if len(pending[digit]) != 0:
            for i in range(len(pending[digit])):
                if pending[digit][i] >= top_elem_idx:
                    break
                pending[digit][i] += 1
                max_shifted_idx = max(max_shifted_idx, pending[digit][i])
    return max_shifted_idx


def get_max_digit(pending, index, swaps_allowed, max_shifted_idx):
    for digit in reversed(range(10)):
        if len(pending[digit]) != 0:
            distance = pending[digit][0] - index
            if distance == 0:
                pending[digit].popleft()
                return digit, swaps_allowed, max_shifted_idx
            elif distance <= swaps_allowed:
                top_elem_idx = pending[digit].popleft()
                max_shifted_idx = get_shifted_idx(pending, top_elem_idx, max_shifted_idx)
                return digit, swaps_allowed - distance, max_shifted_idx


def solve(digits, swaps_allowed):
    pending = [deque() for _ in range(10)]
    for i, digit in enumerate(digits):
        pending[digit].append(i)
    result = []
    shifted_idx = -1
    for i in range(len(digits)):
        digit, swaps_allowed, shifted_idx = get_max_digit(pending, i, swaps_allowed, shifted_idx)
        result.append(digit)
        if swaps_allowed == 0 and i > shifted_idx:
            break
    result.extend(digits[len(result):])
    return ''.join(str(x) for x in result)


t = int(input())
for _ in range(t):
    n, k = map(int, stdin.readline().strip().split())
    a = list(map(int, stdin.readline().strip().split()))
    print(solve(a, k))
