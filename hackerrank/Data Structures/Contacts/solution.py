#!/bin/python3

import os


#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

def contacts(queries):
    # Write your code here
    from collections import Counter

    counter = Counter()
    for operation, word in queries:
        if operation == 'add':
            for i in range(1, len(word) + 1):
                counter.update([word[0:i]])
        elif operation == 'find':
            yield counter[word]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
