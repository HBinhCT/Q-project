#!/bin/python3

import os


# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    from collections import Counter

    # counting characters in s
    counter = Counter(s)
    # number of each character needed in the final string
    chars = {char: count // 2 for char, count in counter.items()}
    # number of each characters needed in shuffling the original string
    shuffled = chars.copy()
    res = []
    for c in reversed(s):
        if chars[c]:
            # Checking if this character should appear before any previous ones.
            # Basically, if this char is smaller than the previous char,
            # and the previous char still occurs in the chars of the shuffled string,
            # then the previous char can safely replace it with this char.
            # That's so because it should be able to still create a valid string
            # which contains both characters although the order will differs.
            while res and res[-1] > c and shuffled[res[-1]] > 0:
                removed_char = res.pop()
                chars[removed_char] += 1
                shuffled[removed_char] -= 1
            res.append(c)
            chars[c] -= 1
        else:
            shuffled[c] -= 1
    return ''.join(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
