#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    # Write your code here
    from collections import deque

    visited = set()
    count = 0
    queue = deque([(n, count)])
    while queue:
        data, count = queue.popleft()
        if data <= 1:
            if data == 1:
                count += 1
            break
        if data - 1 not in visited:
            queue.append((data - 1, count + 1))
            visited.add(data - 1)
        sqr = int(math.sqrt(data))
        for i in range(sqr, 1, -1):
            if data % i == 0:
                div = max(int(data / i), i)
                if div not in visited:
                    visited.add(div)
                    queue.append((div, count + 1))
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
