#!/bin/python3

import os


# Complete the timeInWords function below.
def timeInWords(h, m):
    times = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen',
        'twenty',
    ]
    for i in range(1, 10):
        times.append(f'twenty {times[i - 1]}')
    formats = ["{} o' clock", "quarter past {}", "half past {}", "quarter to {}"]
    hour = times[h - 1] if (m < 31) else times[h]
    if m % 15 == 0:
        return formats[m // 15].format(hour)
    if m < 30:
        return f"{times[m - 1]} minute{'s' * (m != 1)} past {hour}"
    return f"{times[60 - m - 1]} minute{'s' * (m != 59)} to {hour}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
